#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from aiohttp.web import Application

from pkgs.controllers import Controller
from pkgs.middlewares import add_security_headers


async def create_app():
    app = Application(middlewares=[add_security_headers])
    controller = Controller()
    app.add_routes(controller.routes())
    return app
