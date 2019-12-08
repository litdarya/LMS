import json

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


class UserInfoHandler(RequestHandler):
    def initialize(self, user, student):
        body = json.loads(self.request.body)
        self.user_id = body.get('user_id')
        self.user = user(user_id=self.user_id)
        self.student = student(user_id=self.user_id)

    def _bad_request(self, *, msg):
        self.set_status(400)
        self.write({
            'status': 'err',
            'msg': msg
        })
        self.finish()

    async def prepare(self):
        if self.user_id is None:
            self._bad_request(msg='expected user_id in post body')

    async def post(self):
        if await self.user.is_professor:
            self.info = await self.user.get_info()
            self.info['role'] = 'professor'
        else:
            self.info = await self.student.get_info()
            self.info['role'] = 'student'
        self.write({
            'status': 'ok',
            'info': self.info,
        })


class EditUserInfoHandler(RequestHandler):
    def initialize(self, user):
        body = json.loads(self.request.body)
        self.user_id = body.get('user_id')
        self.update = body.get('update')
        self.user = user(user_id=self.user_id)

    def _bad_request(self, *, msg):
        self.set_status(400)
        self.write({
            'status': 'err',
            'msg': msg
        })
        self.finish()

    def prepare(self):
        if self.user_id is None:
            self._bad_request(msg='expected user_id in post body')
        for param in self.update:
            if param not in self.user.DEFAULT_PARAMS:
                self._bad_request(msg=f'unexpected field {param} for user')

    async def post(self):
        updated = await self.user.update_info(update=self.update)
        if updated:
            self.write({
                'status': 'ok',
                'updated': updated
            })
        else:
            self.write({
                'status': '¯\\_(ツ)_/¯',
            })



class GroupHandler(RequestHandler):
    _response = {
        'status': 'ok',
        'group': [],
    }

    async def get(self):
        res = await pe.fetch(
            query="SELECT group_name, department, course_no FROM student_group"
        )
        groups = []
        for record in res:
            groups.append(dict(record))
        self.write({
            'groups': groups
        })
        self.set_status(200)
        self.finish()
