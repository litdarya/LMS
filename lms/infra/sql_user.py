from typing import Iterable, Dict, List

from lms.domain.user import User
# from lms.infra.sql_student import SqlStudent
# from lms.infra.sql_professor import SqlProfessor
import lms.infra.db.postgres_executor as pe


class SqlUser(User):
    def __init__(self, *, user_id):
        super().__init__(user_id=user_id)

    @staticmethod
    async def check_is_professor(*, user_id) -> bool:
        query = "SELECT user_id FROM professors WHERE user_id = $1"
        resolved_user_id = await pe.fetch_val(
            query=query,
            params=(user_id,)
        )
        return resolved_user_id is not None

    async def get_info(
            self,
            *,
            params: Iterable[str] = User.DEFAULT_PARAMS
    ):
        query = f"""SELECT * FROM users WHERE user_id=$1"""
        records = await pe.fetch(
            query=query,
            params=(self.user_id,)
        )
        for record in records:
            user = {}
            for param in params:
                user[param] = record.get(param, None)
            return user
        return None

    async def update_info(
            self,
            *,
            update: Dict
    ):
        fields = list(update.keys() & User.EDITABLE_PARAMS)
        fields_str = ", ".join(fields)
        fields_values = tuple([update[field] for field in fields])
        values_placeholders = ", ".join([f"${i + 2}" for i in range(len(fields))])
        query = f"""
        UPDATE users 
        SET ({fields_str}) = ROW({values_placeholders}) 
        WHERE user_id=$1 
        RETURNING user_id """
        updated_user_id = await pe.fetch_val(
            query=query,
            params=(self.user_id,) + fields_values)
        if updated_user_id:
            return True
        return False
