#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os

import aioredis
from aiohttp.web import Application
from aioredis import Redis

from pkgs.controllers import Controller
from pkgs.middlewares import add_security_headers
from pkgs.jobs import MetricJob
from pkgs.repositories import LastAccessTimeRepository

METRIC_JOB_KEY = 'metric_job'


async def create_app() -> Application:
    app = Application(middlewares=[add_security_headers])
    if 'REDIS_URL' in os.environ:
        redis = await aioredis.create_redis_pool(os.environ['REDIS_URL'])
    else:
        redis = await aioredis.create_redis_pool('redis://localhost')

    last_access_time_repository = LastAccessTimeRepository(redis)
    controller = Controller(last_access_time_repository)
    if 'MACKEREL_API_KEY' in os.environ:
        api_key = os.environ['MACKEREL_API_KEY']
        metric_job = MetricJob(last_access_time_repository, api_key)
        app[METRIC_JOB_KEY] = metric_job

    app.add_routes(controller.routes())
    app.on_cleanup.append(on_cleanup_factory(redis))
    return app


def on_cleanup_factory(redis: Redis):
    async def on_cleanup(_: Application):
        redis.close()
        await redis.wait_closed()

    return on_cleanup
