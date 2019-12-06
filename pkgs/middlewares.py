#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from aiohttp.web import middleware

SECURITY_HEADERS = {
    'Cache-Control': 'private, no-cache, no-store, must-revalidate',
    'Server': 'nginx',
    'X-XSS-Protection': '1; mode=block',
    'X-Frame-Options': 'DENY',
    'X-Content-Type-Options': 'nosniff',
}

@middleware
async def add_security_headers(request, handler):
    response = await handler(request)
    response.headers.extend(SECURITY_HEADERS)
    return response
