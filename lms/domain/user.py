from abc import ABCMeta, abstractmethod
from typing import Dict, List


class User(metaclass=ABCMeta):
    DEFAULT_PARAMS = (
        'name',
        'email',
        'telephone',
        'city',
        'info',
        'vk_link',
        'instagram_link',
        'fb_link',
        'linkedin_link',
    )
    EDITABLE_PARAMS = (
        'telephone',
        'city',
        'info',
        'vk_link',
        'instagram_link',
        'fb_link',
        'linkedin_link',
    )

    def __init__(self, *, user_id):
        self.user_id = user_id

    @abstractmethod
    async def get_info(
            self,
            *,
            params=DEFAULT_PARAMS
    ):
        pass

    @property
    @abstractmethod
    async def is_professor(self):
        pass

    @abstractmethod
    async def courses_list(self) -> List[Dict[str, str]]:
        pass

    @abstractmethod
    async def update_info(
            self,
            *,
            update: Dict
    ):
        pass
