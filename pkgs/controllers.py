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

from pkgs.repositories import AccessCountRepository


class Controller:
    def __init__(self, access_log_repository: AccessCountRepository):
        self._access_log_repository = access_log_repository

    def routes(self) -> List[RouteDef]:
        return [
            web.get('/health', self.health),
            web.get('/favicon.ico', self.not_found),
            web.get('/robots.txt', self.not_found),
            web.get('/sitemap.xml', self.not_found),
            web.get('/{path:.*}', self.redirect),
        ]

    async def health(self, _: Request) -> Response:
        return Response(
            body='OK',
            content_type='text/plain',
            charset='utf-8'
        )

    async def redirect(self, request: Request) -> Response:
        await self._access_log_repository.increment()

        path = request.match_info['path']
        return HTTPMovedPermanently(
            'https://emoji-gen.ninja/{}'.format(path)
        )

    async def not_found(self, _: Request) -> Response:
        return HTTPNotFound()
