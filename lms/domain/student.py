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
        return super().properties() + self.EXTRA_STUDENT_PROPERTIES

    @staticmethod
    def hidden_properties():
        return ('education_form', )

    @property
    async def is_professor(self):
        return False
