import click
from tornado import ioloop
from tornado.web import Application

from lms.web.urls import get_all_urls
from tornado_sqlalchemy import make_session_factory

# DB_ADDR = 'postgres://user:password@host/database'


class LmsApplication(Application):
    def __init__(self, handlers, **kwargs):
        super(LmsApplication, self).__init__(handlers=handlers, **kwargs)
        self.db_session = None

    def prepare(self):
        self.db_session = make_session_factory(DB_ADDR)


@click.command()
@click.option('--port', default=8001)
def serve(port: int):
    handlers = get_all_urls()
    application = LmsApplication(handlers)
    application.listen(port)
    application.prepare()
    ioloop.IOLoop.current().start()


if __name__ == '__main__':
    serve()
