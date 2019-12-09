#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from datetime import datetime
from typing import List

from aiohttp import web
from aiohttp.web import (
    HTTPMovedPermanently,
    HTTPNotFound,
    Request,
    Response,
    RouteDef,
)

from pkgs.repositories import LastAccessTimeRepository


class Controller:
    def __init__(self, last_access_time_repository: LastAccessTimeRepository):
        self._last_access_time_repository = last_access_time_repository

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
            charset='utf-8',
            headers={
                'Cache-Control': 'private, no-cache, no-store, must-revalidate',
            }
        )

    async def redirect(self, request: Request) -> Response:
        now = datetime.now()
        await self._last_access_time_repository.set(now)

        path = request.match_info['path']
        return HTTPMovedPermanently(
            'https://emoji-gen.ninja/{}'.format(path),
            headers={
                'Cache-Control': 'public, max-age=10',
            }
        )

    async def not_found(self, _: Request) -> Response:
        return HTTPNotFound(
            headers={
                'Cache-Control': 'public, max-age=10',
            }
        )
