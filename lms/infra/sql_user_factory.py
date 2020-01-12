# pylint: disable=too-few-public-methods

from typing import Union

from lms.domain.user_factory import UserFactory
from lms.infra.sql_professor import SqlProfessor
from lms.infra.sql_student import SqlStudent
from lms.infra.sql_user import SqlUser


class SqlUserFactory(UserFactory):
    @staticmethod
    async def get_student_or_professor(user_id) -> Union[SqlStudent, SqlProfessor]:
        professor = await SqlUser.check_is_professor(user_id=user_id)
        if professor:
            return SqlProfessor(user_id=user_id)
        return SqlStudent(user_id=user_id)
