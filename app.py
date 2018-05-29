#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from aiohttp.web import Application, run_app
from aiohttp.web_exceptions import HTTPMovedPermanently


def redirect(request):
    return HTTPMovedPermanently(
        'https://emoji-gen.ninja/',
        headers={
            'Cache-Control': 'public, max-age=600', # 10 min
            'X-XSS-Protection': '1; mode=block',
            'X-Frame-Options': 'DENY',
            'X-Content-Type-Options': 'nosniff',
        },
    )


app = Application()
app.router.add_get('/{path:.*}', redirect)


if __name__ == '__main__':
    run_app(app)
