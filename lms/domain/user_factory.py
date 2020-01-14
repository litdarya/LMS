# pylint: disable=too-few-public-methods

from abc import ABC, abstractmethod
from typing import Union, Optional, Tuple
from lms.domain.student import Student
from lms.domain.professor import Professor


class UserFactory(ABC):
    @staticmethod
    @abstractmethod
    async def get_student_or_professor(
            *,
            user_id: int,
            authenticated=False
    ) -> Union[Student, Professor]:
        pass

    @staticmethod
    @abstractmethod
    async def login_user(*, email: str, password: str) -> Optional[str]:
        pass

    @staticmethod
    @abstractmethod
    async def register_user(
            *,
            verification_code: str,
            email: str,
            password: str
    ) -> Tuple[bool, str]:
        pass
