#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from typing import List

from aiohttp import web
from aiohttp.web import (
    HTTPMovedPermanently,
    HTTPNotFound,
    Request,
    Response,
    RouteDef,
)


def routes() -> List[RouteDef]:
    return [
        web.get('/health', health),
        web.get('/favicon.ico', not_found),
        web.get('/robots.txt', not_found),
        web.get('/sitemap.xml', not_found),
        web.get('/{path:.*}', redirect),
    ]


async def health(_: Request) -> Response:
    return Response(
        body='OK',
        content_type='text/plain',
        charset='utf-8'
    )


async def redirect(request: Request) -> Response:
    path = request.match_info['path']
    return HTTPMovedPermanently(
        'https://emoji-gen.ninja/{}'.format(path)
    )


async def not_found(_: Request) -> Response:
    return HTTPNotFound()
