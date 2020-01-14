from typing import List, Tuple
from tornado.web import RequestHandler
from lms.infra.sql_user_factory import SqlUserFactory

from lms.web.handlers import (
    PingHandler,
    GroupHandler,
    UserInfoHandler,
    UserCoursesHandler,
    EditUserInfoHandler,
)

PING_URL = (r'/ping', PingHandler)
URLS = [
    (r'/list_groups/', GroupHandler),
    (r'/user_info/', UserInfoHandler, dict(user_factory=SqlUserFactory)),
    (r'/user_courses/', UserCoursesHandler, dict(user_factory=SqlUserFactory)),
    (r'/edit_user_info/', EditUserInfoHandler, dict(user_factory=SqlUserFactory))
]


def get_all_urls() -> List[Tuple[str, RequestHandler]]:
    return [PING_URL] + URLS
