import json
from tornado.web import RequestHandler


class PingHandler(RequestHandler):
    _response = {
        'status': 'ok'
    }

    def get(self):
        self.write(self._response)
        self.set_status(200)
        self.finish()


class GroupHandler(RequestHandler):
    _response = {
        ''
        'status': 'ok'
    }

    def get(self):
        self.write(self._response)
        self.set_status(200)
        self.finish()
