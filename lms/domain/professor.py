# pylint: disable=abstract-method

from abc import ABCMeta
from lms.domain.user import User


class Professor(User, metaclass=ABCMeta):
    @property
    async def is_professor(self):
        return True
