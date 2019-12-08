from tornado.web import RequestHandler
from typing import List, Tuple, Type

from lms.web.handlers import (
    PingHandler,
    GroupHandler,
)

ping_url = (r'/ping', PingHandler)
urls = [
        (r'/list_groups/', GroupHandler)
    ]


def get_all_urls() -> List[Tuple[str, RequestHandler]]:
    return [ping_url] + urls
