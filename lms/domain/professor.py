from abc import abstractmethod
from lms.domain.user import User


class Professor(User):
    DEFAULT_PARAMS = User.DEFAULT_PARAMS

    @property
    async def is_professor(self):
        return True

    @abstractmethod
    async def get_info(
            self,
            *,
            params=('name', 'email', 'telephone', 'city', 'info', 'vk_link')
    ):
        pass
