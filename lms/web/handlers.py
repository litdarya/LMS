import json

import tornado.escape
from tornado.web import RequestHandler

import lms.infra.db.postgres_executor as pe

class PingHandler(RequestHandler):
    _response = {
        'status': 'ok',
    }

    def get(self):
        self.write(self._response)
        self.set_status(200)
        self.finish()


class GroupHandler(RequestHandler):
    _response = {
        'status': 'ok',
        'group': [],
    }

    async def get(self):
        res = await pe.execute(
            query="SELECT name, department, course_num FROM student_group "
            "where name = $1 or 1=1",
            params=("CV",))
        groups = []
        for record in res:
            groups.append({
                'name': record.get('name'),
                'department': record.get('department'),
                'course_num': record.get('course_num'),
            })
            print(type(groups[-1]['department']))
        print(groups)
        self.write({
            'groups': groups
        })
        self.set_status(200)
        self.finish()
