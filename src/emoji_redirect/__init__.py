#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from aiohttp.web import Application, Response
from aiohttp.web_exceptions import HTTPMovedPermanently, HTTPNotFound


security_headers = {
    'X-XSS-Protection': '1; mode=block',
    'X-Frame-Options': 'DENY',
    'X-Content-Type-Options': 'nosniff',
}


async def healthcheck(request):
    return Response(
        body='OK',
        headers={
            'Cache-Control': 'private, no-cache, no-store, must-revalidate',
            **security_headers,
        },
        content_type='text/plain',
        charset='utf-8'
    )


async def redirect(request):
    path = request.match_info['path']
    return HTTPMovedPermanently(
        'https://emoji-gen.ninja/{}'.format(path),
        headers={
            'Cache-Control': 'private, no-cache, no-store, must-revalidate',
            **security_headers,
        },
    )


async def not_found(request):
    return HTTPNotFound()


def provide_app():
    app = Application()
    app.router.add_get('/healthcheck', healthcheck)
    app.router.add_get('/favicon.ico', not_found)
    app.router.add_get('/robots.txt', not_found)
    app.router.add_get('/sitemap.xml', not_found)
    app.router.add_get('/{path:.*}', redirect)
    return app
