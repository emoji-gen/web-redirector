#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from aiohttp.web import Application, Response, run_app
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
            'Cache-Control': 'private, no-store, no-cache, must-revalidate',
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
            'Cache-Control': 'public, max-age=600', # 10 min
            **security_headers,
        },
    )


async def not_found(request):
    return HTTPNotFound()


def app_provider():
    app = Application()
    app.router.add_get('/healthcheck', healthcheck)
    app.router.add_get('/favicon.ico', not_found)
    app.router.add_get('/robots.txt', not_found)
    app.router.add_get('/sitemap.xml', not_found)
    app.router.add_get('/{path:.*}', redirect)
    return app
