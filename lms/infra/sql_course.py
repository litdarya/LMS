from typing import Dict, Optional, Iterable
import lms.infra.db.postgres_executor as pe


class SqlCourse(object):
    def __init__(self, *, course_id):
        self.course_id = course_id

    async def get_info(self) -> Optional[Dict[str, str]]:
        query = '''SELECT course_id, name, description FROM course WHERE course_id = $1'''
        record = await pe.fetch_row(
            query=query,
            params=(self.course_id,)
        )
        if record is None:
            return None
        return dict(record)

    @staticmethod
    async def resolve_courses(*, course_ids: Iterable[int]):
        courses = []
        for course_id in course_ids:
            assert course_id is not None
            course = SqlCourse(course_id=course_id)
            info = await course.get_info()
            courses.append(info)
        return courses
