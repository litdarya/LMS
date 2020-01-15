from abc import ABCMeta, abstractmethod
from typing import Dict, Iterable, List, Optional, Any

from lms.domain.course_material import CourseMaterial
from lms.domain.professor import Professor
from lms.domain.user import User


class Course(metaclass=ABCMeta):
    NATIVE_PROPERTIES = (
        'course_id',
        'name',
        'description',
    )
    ADDITIONAL_PROPERTIES = (
        'professors',
        'editors',
        'materials',
        'assignees',
    )
    PROPERTIES = NATIVE_PROPERTIES + ADDITIONAL_PROPERTIES

    def __init__(self, *, course_id):
        self.course_id = course_id

    @abstractmethod
    async def get_professors(self) -> List[Professor]:
        pass

    @abstractmethod
    async def get_editors(self) -> List[User]:
        pass

    @abstractmethod
    async def get_materials(self) -> List[CourseMaterial]:
        pass

    @staticmethod
    async def get_assignees():
        return []

    async def get_additional_info(self, properties: List[str]) -> Dict[str, Any]:
        info = {}
        if 'professors' in properties:
            info['professors'] = self.get_professors()
        if 'editors' in properties:
            info['editors'] = self.get_editors()
        if 'materials' in properties:
            info['materials'] = self.get_materials()
        if 'assignees' in properties:
            info['assignees'] = self.get_assignees()
        return info

    @abstractmethod
    async def get_info(
            self,
            *,
            properties: Optional[Iterable[str]] = None
    ) -> Optional[Dict[str, Any]]:
        pass
