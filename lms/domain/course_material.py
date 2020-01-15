# pylint: disable=too-few-public-methods

from abc import ABCMeta


class CourseMaterial(metaclass=ABCMeta):
    PROPERTIES = (
        'course_id',
        'name',
        'description',
        'add_time',
    )
