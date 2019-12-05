#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from aiohttp.web import (
    Application,
    HTTPMovedPermanently,
    HTTPNotFound,
    Response,
)


# ---------------------------------------------------------
# Handlers
# ---------------------------------------------------------

HEADERS = {
    'Cache-Control': 'private, no-cache, no-store, must-revalidate',
    'Server': 'nginx',
    'X-XSS-Protection': '1; mode=block',
    'X-Frame-Options': 'DENY',
    'X-Content-Type-Options': 'nosniff',
}

async def health(request):
    return Response(
        body='OK',
        headers=HEADERS,
        content_type='text/plain',
        charset='utf-8'
    )

async def redirect(request):
    path = request.match_info['path']
    return HTTPMovedPermanently(
        'https://emoji-gen.ninja/{}'.format(path),
        headers=HEADERS,
    )

async def not_found(request):
    return HTTPNotFound(headers=HEADERS)


# ---------------------------------------------------------
# Routes
# ---------------------------------------------------------

async def create_app():
    app = Application()
    app.router.add_get('/health', health)
    app.router.add_get('/favicon.ico', not_found)
    app.router.add_get('/robots.txt', not_found)
    app.router.add_get('/sitemap.xml', not_found)
    app.router.add_get('/{path:.*}', redirect)
    return app
