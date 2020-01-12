from abc import abstractmethod
from lms.domain.user import User


class Student(User):
    EXTRA_STUDENT_PARAMS = (
        'group_name',
        'entry_year',
        'degree',
        'study_form',
        'education_form',
    )
    DEFAULT_PARAMS = (
        User.DEFAULT_PARAMS +
        EXTRA_STUDENT_PARAMS
    )

    @property
    async def is_professor(self):
        return False

    @abstractmethod
    async def get_info(
            self,
            *,
            params=('name', 'email', 'telephone', 'city', 'info', 'vk_link')
    ):
        pass
