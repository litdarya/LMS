from abc import ABCMeta, abstractmethod
from typing import Dict, Iterable, List, Optional


class User(metaclass=ABCMeta):
    USER_PROPERTIES = (
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
    EDITABLE_USER_PROPERTIES = (
        'telephone',
        'city',
        'info',
        'vk_link',
        'instagram_link',
        'fb_link',
        'linkedin_link',
    )

    def properties(self):
        return self.USER_PROPERTIES

    def editable_properties(self):
        return self.EDITABLE_USER_PROPERTIES

    @staticmethod
    def hidden_properties():
        return tuple()

    def __init__(self, *, user_id, authenticated=False):
        self.user_id = user_id
        self.authenticated = authenticated

    @abstractmethod
    async def get_info(
            self,
            *,
            properties: Optional[Iterable[str]] = None
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
