from tornado.web import RequestHandler
from typing import List, Tuple, Type
from lms.infra.sql_user import SqlUser
from lms.infra.sql_student import SqlStudent

from lms.web.handlers import (
    PingHandler,
    GroupHandler,
    UserInfoHandler,
    EditUserInfoHandler,
)

ping_url = (r'/ping', PingHandler)
urls = [
    (r'/list_groups/', GroupHandler),
    (r'/user_info/', UserInfoHandler, dict(user=SqlUser, student=SqlStudent)),
    (r'/edit_user_info/', EditUserInfoHandler, dict(user=SqlUser))
]


def get_all_urls() -> List[Tuple[str, RequestHandler]]:
    return [ping_url] + urls
