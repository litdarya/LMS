from abc import ABC, abstractmethod
from lms.domain.user import User


class Student(User):
    DEFAULT_PARAMS = (
        *User.DEFAULT_PARAMS,
        'group_name',
        'entry_year',
        'degree',
        'study_form',
        'education_form',
    )

    def __init__(self, *, user_id):
        super().__init__(user_id=user_id)

    @abstractmethod
    async def get_info(
            self,
            *,
            params=('name', 'email', 'telephone', 'city', 'info', 'vk_link')
    ):
        pass
