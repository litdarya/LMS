from typing import Iterable, List, Dict

from lms.domain.student import Student
from lms.infra.sql_course import SqlCourse
from lms.infra.sql_user import SqlUser
import lms.infra.db.postgres_executor as pe


class SqlStudent(SqlUser, Student):
    async def get_info(
            self,
            *,
            params: Iterable[str] = Student.DEFAULT_PARAMS
    ):
        extra_fields = set(params) & set(Student.EXTRA_STUDENT_PARAMS)
        user_fields = list(set(params) & set(SqlUser.DEFAULT_PARAMS))
        query = """
            SELECT *
            FROM student
            WHERE student.user_id = $1
        """
        record_future = pe.fetch_row(
            query=query,
            params=(self.user_id,)
        )
        student_info_future = SqlUser.get_info(self, params=user_fields)
        record = await record_future
        if record is None:
            return None
        student_info = await student_info_future

        assert student_info is not None, 'have row in students table but not in users'
        for field in extra_fields:
            student_info[field] = record.get(field, None)
        student_info['role'] = 'student'
        return student_info

    async def courses_list(self) -> List[Dict[str, str]]:
        print('student')
        info = await self.get_info(params=('group_name',))
        group_name = info.get('group_name')
        if group_name is None:
            print('no group name')
            return []
        print(group_name)
        query_courses = '''SELECT course_id
            FROM group_to_course 
            WHERE group_name = $1'''
        records = await pe.fetch(
            query=query_courses,
            params=(group_name,)
        )
        if records is None:
            return []
        courses = await SqlCourse.resolve_courses(
            course_ids=[record.get('course_id', None) for record in records]
        )
        return courses
