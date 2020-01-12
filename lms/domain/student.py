# pylint: disable=abstract-method

from abc import ABCMeta

from lms.domain.user import User


class Student(User, metaclass=ABCMeta):
    EXTRA_STUDENT_PROPERTIES = (
        'group_name',
        'entry_year',
        'degree',
        'study_form',
        'education_form',
    )

    def properties(self):
        return User.properties(self) + self.EXTRA_STUDENT_PROPERTIES

    @property
    async def is_professor(self):
        return False

    # params=('name', 'email', 'telephone', 'city', 'info', 'vk_link')
