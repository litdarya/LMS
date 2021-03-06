from typing import Iterable, List, Optional

from lms.domain.course import Course
from lms.domain.professor import Professor

from lms.infra.sql_course import SqlCourse
from lms.infra.sql_user import SqlUser
import lms.infra.db.postgres_executor as pe


class SqlProfessor(SqlUser, Professor):
    async def get_info(
            self,
            *,
            properties: Optional[Iterable[str]] = None
    ):
        if properties is None:
            properties = self.properties()
        professor_info = await SqlUser.get_info(self, properties=properties)
        if professor_info and 'role' in properties:
            professor_info['role'] = 'professor'
        return professor_info

    async def courses(self) -> List[Course]:
        query_course_ids = '''SELECT course_id
        FROM course_to_professor
        WHERE professor_id = $1'''
        records = await pe.fetch(
            query=query_course_ids,
            params=(self.user_id,)
        )
        if records is None:
            return []
        courses = [
            SqlCourse(course_id=record.get('course_id'))
            for record in records
        ]
        return courses
