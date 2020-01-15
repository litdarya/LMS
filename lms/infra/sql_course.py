from typing import Dict, Optional, Iterable, Any, List
import lms.infra.db.postgres_executor as pe
from lms.domain.course import Course
from lms.domain.course_material import CourseMaterial
from lms.domain.professor import Professor
from lms.domain.user import User


class SqlCourse(Course):
    async def get_professors(self) -> List[Professor]:
        return []

    async def get_editors(self) -> List[User]:
        return []

    async def get_materials(self) -> List[CourseMaterial]:
        return []

    async def get_info(
            self,
            *,
            properties: Optional[Iterable[str]] = None
    ) -> Optional[Dict[str, Any]]:
        if properties is None:
            properties = self.PROPERTIES
        query = '''SELECT course_id, name, description FROM course WHERE course_id = $1'''
        record = await pe.fetch_row(
            query=query,
            params=(self.course_id,)
        )
        if record is None:
            return None
        info = {}
        for key in record.keys():
            if key in properties:
                info[key] = record.get(key)
        additional_info = await self.get_additional_info(properties)
        info.update(additional_info)
        return info
