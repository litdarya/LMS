# pylint: disable=too-few-public-methods

from typing import Union, Optional, Tuple

from lms.domain.user_factory import UserFactory
from lms.infra.sql_professor import SqlProfessor
from lms.infra.sql_student import SqlStudent
from lms.infra.sql_user import SqlUser


class SqlUserFactory(UserFactory):
    @staticmethod
    async def get_student_or_professor(
            *,
            user_id: int,
            authenticated=False
    ) -> Union[SqlStudent, SqlProfessor]:
        professor = await SqlUser.check_is_professor(user_id=user_id)
        if professor:
            return SqlProfessor(user_id=user_id, authenticated=authenticated)
        return SqlStudent(user_id=user_id, authenticated=authenticated)

    @staticmethod
    async def login_user(*, email: str, password: str) -> Optional[str]:
        return await SqlUser.login(email=email, password=password)

    @staticmethod
    async def register_user(
            *,
            verification_code: str,
            email: str,
            password: str
    ) -> Tuple[bool, str]:
        pass
