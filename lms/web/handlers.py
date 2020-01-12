# pylint: disable=abstract-method
# pylint: disable=arguments-differ

import json
from abc import abstractmethod

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


class UserHandler(RequestHandler):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.body = None
        self.user_id = None
        self.user_factory = None
        self.user = None

    def initialize(self, user_factory):
        self.body = json.loads(self.request.body)
        self.user_id = self.body.get('user_id')
        self.user_factory = user_factory

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
        self.user = await self.user_factory.get_student_or_professor(
            user_id=self.user_id
        )

    @abstractmethod
    async def post(self, *args, **kwargs):
        pass


class UserInfoHandler(UserHandler):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.info = None

    async def post(self):
        self.info = await self.user.get_info()
        self.write({
            'status': 'ok',
            'info': self.info,
        })


class UserCoursesHandler(UserHandler):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.courses = None

    async def post(self):
        self.courses = await self.user.courses_list()
        self.write({
            'status': 'ok',
            'courses': self.courses,
        })


class EditUserInfoHandler(UserHandler):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.update = None

    def initialize(self, user_factory):
        super().initialize(user_factory)
        self.update = self.body.get('update')

    async def prepare(self):
        await super().prepare()
        if not self.update:
            self._bad_request(msg='expected "update" parameter')
        for param in self.update:
            if param not in self.user.EDITABLE_PARAMS:
                self._bad_request(
                    msg=f'unexpected field {param} does not exist or cannot be updated'
                )

    async def post(self, *args, **kwargs):
        updated = await self.user.update_info(update=self.update)
        if updated:
            self.write({
                'status': 'ok',
                'updated': updated,
            })
        else:
            self.write({
                'status': 'error',
                'updated': 'false',
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
