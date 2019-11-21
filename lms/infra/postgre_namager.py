from builtins import property


class PostgreManager:
    def __init__(self, session):
        self.session = session

        self.prepared_queries = {
            '': self._prepare_get_all_groups,
        }

    @property
    def _prepare_get_all_groups(self):
        query = '''SELECT name,department, course_num
        FROM student_group
        LIMIT 100;
        '''
        return self.session.prepare(query)
