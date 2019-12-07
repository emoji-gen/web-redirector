#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from aiohttp.web import Application

from pkgs.controller import routes
from pkgs.middlewares import add_security_headers


async def create_app() -> Application:
    app = Application(middlewares=[add_security_headers])
    app.add_routes(routes())
    return app
