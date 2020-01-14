from typing import Iterable, List, Dict, Optional

from lms.domain.student import Student
from lms.domain.user import User
from lms.infra.sql_course import SqlCourse
from lms.infra.sql_user import SqlUser
import lms.infra.db.postgres_executor as pe


def update_dict_with_keys(dict_to_update: dict, other_dict: dict, keys):
    for key in keys:
        dict_to_update[key] = other_dict[key]
    return dict_to_update


class SqlStudent(SqlUser, Student):
    async def _get_extra_student_info(self, *, properties: Iterable[str]):
        query = """
            SELECT *
            FROM student
            WHERE student.user_id = $1
        """
        student_info_record_future = pe.fetch_row(
            query=query,
            params=(self.user_id,)
        )
        student_info_record = await student_info_record_future
        if student_info_record is None:
            return None
        return update_dict_with_keys({}, dict(student_info_record), properties)

    async def get_info(
            self,
            *,
            properties: Optional[Iterable[str]] = None
    ):
        properties = set(properties)
        if not properties.issubset(self.properties()):
            return ValueError("parameter properties is not subset of student properties")

        extra_fields = properties & set(Student.EXTRA_STUDENT_PROPERTIES)
        user_fields = list(properties & set(User.properties(self)))
        user_info_future = SqlUser.get_info(self, properties=user_fields)
        student_info_future = self._get_extra_student_info(properties=extra_fields)
        user_info = await user_info_future
        student_info = await student_info_future
        if student_info is None:
            return None
        assert user_info is not None, 'have row in students table but not in users'
        student_info.update(user_info)
        return student_info

    async def courses_list(self) -> List[Dict[str, str]]:
        print('student')
        info = await self.get_info(properties=('group_name',))
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
