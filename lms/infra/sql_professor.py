from typing import Iterable

from lms.domain.professor import Professor
from lms.infra.sql_user import SqlUser
import lms.infra.db.postgres_executor as pe


class SqlProfessor(SqlUser, Professor):
    def __init__(self, *, user_id):
        super().__init__(user_id=user_id)

    async def get_info(
            self,
            *,
            params: Iterable[str] = Professor.DEFAULT_PARAMS
    ):
        professor_info = await SqlUser.get_info(self, params=params)
        if professor_info:
            professor_info['role'] = 'professor'
        return professor_info
