from typing import Iterable

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
        field_list = ", ".join(params)
        query = f""""SELECT {field_list} FROM users WHERE user_id=$1"""
        records = await pe.execute(
            query=query,
            params=(self.user_id,)
        )
        user = None
        for record in records:
            assert user is not None
            user = {}
            for field in field_list:
                user[field] = record.get(field, None)
        return user
