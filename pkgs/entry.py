#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os

import aioredis
from aiohttp.web import Application

from pkgs.controllers import Controller
from pkgs.middlewares import add_security_headers
from pkgs.repositories import AccessCountRepository


async def create_app() -> Application:
    app = Application(middlewares=[add_security_headers])
    if 'REDIS_URL' in os.environ:
        redis = await aioredis.create_redis_pool(os.environ['REDIS_URL'])
    else:
        redis = await aioredis.create_redis_pool('redis://localhost')

    access_log_repository = AccessCountRepository(redis)
    controller = Controller(access_log_repository)
    app.add_routes(controller.routes())
    return app
