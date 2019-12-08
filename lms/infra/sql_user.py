from typing import Iterable, Dict

from lms.domain.user import User
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
        records = await pe.fetch(
            query=query,
            params=(self.user_id,)
        )
        for record in records:
            assert record.get('user_id') is not None
            return True
        return False

    async def update_info(
            self,
            *,
            update: Dict
    ):
        fields = list(update.keys() & User.EDITABLE_PARAMS)
        fields_str = ", ".join(fields)
        fields_values = tuple([update[field] for field in fields])
        values_placeholders =  ", ".join([f"${i + 2}" for i in range(len(fields))])
        query = f"""
        UPDATE users 
        SET ({fields_str}) = ROW({values_placeholders}) 
        WHERE user_id=$1 """
        print(query, (self.user_id,) + fields_values)
        record = await pe.fetch_val(
            query=query,
            params=(self.user_id,) + fields_values)
        print('record=', record)
        if record:
            return dict(record)
        return None
