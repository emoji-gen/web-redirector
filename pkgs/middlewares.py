#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from typing import Callable

from aiohttp.web import (
    middleware,
    Request,
    Response,
)

SECURITY_HEADERS = {
    'Server': 'nginx',
    'X-XSS-Protection': '1; mode=block',
    'X-Frame-Options': 'DENY',
    'X-Content-Type-Options': 'nosniff',
}


@middleware
async def add_security_headers(request: Request, handler: Callable) -> Response:
    response: Response = await handler(request)
    response.headers.extend(SECURITY_HEADERS)
    return response
