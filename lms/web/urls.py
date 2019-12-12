from tornado.web import RequestHandler
from typing import List, Tuple, Type
from lms.infra.sql_user_factory import SqlUserFactory

from lms.web.handlers import (
    PingHandler,
    GroupHandler,
    UserInfoHandler,
    EditUserInfoHandler,
)

ping_url = (r'/ping', PingHandler)
urls = [
    (r'/list_groups/', GroupHandler),
    (r'/user_info/', UserInfoHandler, dict(user_factory=SqlUserFactory)),
    (r'/edit_user_info/', EditUserInfoHandler, dict(user_factory=SqlUserFactory))
]


def get_all_urls() -> List[Tuple[str, RequestHandler]]:
    return [ping_url] + urls
