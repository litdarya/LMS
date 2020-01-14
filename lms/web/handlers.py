# pylint: disable=abstract-method
# pylint: disable=arguments-differ
# pylint: disable=attribute-defined-outside-init

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


class UserHandler(RequestHandler):
    def initialize(self, user_factory):
        self.user_factory = user_factory

    def get_current_user(self):
        return self.get_secure_cookie('user_id')

    def _bad_request(self, status=400, *, msg):
        self.set_status(status)
        self.write({
            'status': 'err',
            'msg': msg
        })
        self.finish()


class GetUserId(UserHandler):
    def get(self):
        user_id = self.get_current_user()
        if user_id:
            user_id = user_id.decode('utf-8')
        self.write({
            'user_id': user_id
        })


class LoginHandler(UserHandler):
    def initialize(self, user_factory):
        super().initialize(user_factory=user_factory)
        self.body = json.loads(self.request.body)
        self.email = self.body.get('email')
        self.password = self.body.get('password')

    def get(self):
        self.write({
            'status': 'err',
            'msg': 'need to login'
        })
        self.finish()

    async def post(self):
        self.body = json.loads(self.request.body)
        user_id = await self.user_factory.login_user(email=self.email, password=self.password)
        if user_id:
            self.set_secure_cookie("user_id", str(user_id))
            self.write({
                'status': 'ok',
                'msg': 'successfully logged in, set cookies in header',
            })
        else:
            self._bad_request(status=401, msg='incorrect email or password')


class RegisterHandler(UserHandler):
    def initialize(self, user_factory):
        super().initialize(user_factory=user_factory)
        self.body = json.loads(self.request.body)
        self.verification_code = self.body.get('verification_code')
        self.email = self.body.get('email')
        self.password = self.body.get('password')

    async def post(self):
        success, msg = await self.user_factory.register_user(
            verification_code=self.verification_code,
            email=self.email,
            password=self.password
        )
        if not success:
            self._bad_request(status=401, msg=msg)
        else:
            self.write({
                'status': 'ok',
                'msg': msg,
            })


class AuthUserHandler(UserHandler):
    def initialize(self, user_factory):
        super().initialize(user_factory=user_factory)
        self.body = json.loads(self.request.body)
        self.user_id = self.body.get('user_id')

    async def prepare(self):
        if self.user_id is None:
            self._bad_request(msg='expected user_id in post body')
        self.user = await self.user_factory.get_student_or_professor(
            user_id=self.user_id
        )


class UserInfoHandler(AuthUserHandler):
    async def post(self):
        self.info = await self.user.get_info()
        self.write({
            'status': 'ok',
            'info': self.info,
        })


class UserCoursesHandler(AuthUserHandler):
    async def post(self):
        self.courses = await self.user.courses_list()
        self.write({
            'status': 'ok',
            'courses': self.courses,
        })


class EditUserInfoHandler(AuthUserHandler):
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

    async def post(self):
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
