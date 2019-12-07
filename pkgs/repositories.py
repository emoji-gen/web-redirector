#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from datetime import date, datetime, timedelta
from typing import List

from aioredis import Redis


class AccessCountRepository:
    TIMEOUT_SECONDS = 60 * 60 * 24 * 7

    def __init__(self, redis: Redis):
        self._redis = redis

    async def increment(self) -> None:
        now = datetime.now()
        key = self._build_key(now.date())
        timestamp = int(now.timestamp() * 1000)

        await self._redis.rpush(key, timestamp)
        await self._redis.expire(key, self.TIMEOUT_SECONDS)

    async def count(self, start: datetime, end: datetime) -> int:
        keys = self._build_keys(start.date(), end.date())

        timestamps: List[int] = []
        for key in keys:
            items: List[bytes] = await self._redis.lrange(key, 0, -1)
            for item in items:
                timestamps.append(int(item.decode('utf-8')))

        total = 0
        start_ts = int(start.timestamp() * 1000)
        end_ts = int(end.timestamp() * 1000)
        for timestamp in timestamps:
            if start_ts <= timestamp < end_ts:
                total += 1

        return total

    @classmethod
    def _build_keys(cls, start: date, end: date) -> List[str]:
        keys = []
        for i in range((end - start).days + 1):
            dt = start + timedelta(i)
            keys.append(cls._build_key(dt))
        return keys

    @classmethod
    def _build_key(cls, dt: date) -> str:
        return 'access_count:{}'.format(dt.strftime('%Y%m%d'))
