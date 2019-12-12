from typing import Iterable, Dict

from lms.domain.user import User
# from lms.infra.sql_student import SqlStudent
# from lms.infra.sql_professor import SqlProfessor
import lms.infra.db.postgres_executor as pe


class SqlUser(User):
    def __init__(self, *, user_id):
        super().__init__(user_id=user_id)

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

    @property
    async def is_professor(self):
        query = "SELECT user_id FROM professors WHERE user_id = $1"
        user_id = await pe.fetch_val(
            query=query,
            params=(self.user_id,)
        )
        if user_id is None:
            return False
        assert user_id == self.user_id
        return True

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
