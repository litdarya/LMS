from typing import Iterable, List, Dict

from lms.domain.professor import Professor
from lms.infra.sql_course import SqlCourse
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

    async def courses_list(self) -> List[Dict[str, str]]:
        print('professor')
        query_course_ids = '''SELECT course_id
        FROM course_to_professor
        WHERE professor_id = $1'''
        records = await pe.fetch(
            query=query_course_ids,
            params=(self.user_id,)
        )
        if records is None:
            return []
        courses = await SqlCourse.resolve_courses(
            course_ids=[record.get('course_id', None) for record in records]
        )
        return courses

