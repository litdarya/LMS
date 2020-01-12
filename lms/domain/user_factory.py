# pylint: disable=too-few-public-methods

from abc import ABC, abstractmethod
from typing import Union
from lms.domain.student import Student
from lms.domain.professor import Professor


class UserFactory(ABC):
    @staticmethod
    @abstractmethod
    async def get_student_or_professor(user_id) -> Union[Student, Professor]:
        pass
