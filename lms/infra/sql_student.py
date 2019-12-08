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
        fields = ", ".join(Student.DEFAULT_PARAMS)
        query = f"""
        SELECT {fields}
        FROM users
            JOIN student 
            ON users.user_id = student.user_id AND users.user_id = $1 AND student.user_id = $1
        """
        records = await pe.fetch(
            query=query,
            params=(self.user_id,)
        )
        for record in records:
            student = {}
            print(dict(record))
            for param in params:
                student[param] = record.get(param, None)
            return student
        return None
