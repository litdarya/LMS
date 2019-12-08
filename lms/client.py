import click
from tornado import ioloop
from tornado.web import Application

from lms.web.urls import get_all_urls


class LmsApplication(Application):
    def __init__(self, handlers, **kwargs):
        super(LmsApplication, self).__init__(handlers=handlers, **kwargs)
        self.db_session = None


@click.command()
@click.option('--port', default=8000)
def serve(port: int):
    handlers = get_all_urls()
    application = LmsApplication(handlers)
    application.listen(port)
    ioloop.IOLoop.current().start()


if __name__ == '__main__':
    serve()
