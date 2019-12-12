from typing import Iterable

from lms.domain.student import Student
from lms.infra.sql_user import SqlUser
import lms.infra.db.postgres_executor as pe


class SqlStudent(SqlUser, Student):
    def __init__(self, *, user_id):
        super().__init__(user_id=user_id)

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
