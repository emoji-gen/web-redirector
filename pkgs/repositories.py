#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from datetime import datetime
from typing import Optional

from aioredis import Redis


class LastAccessTimeRepository:
    KEY = 'last_access_time'
    TIMEOUT_SECONDS = 60 * 60 * 24 * 30

    def __init__(self, redis: Redis):
        self._redis = redis

    async def set(self, dt: datetime) -> None:
        ts = int(dt.timestamp() * 1000)
        await self._redis.set(self.KEY, ts, expire=self.TIMEOUT_SECONDS)

    async def get(self) -> Optional[datetime]:
        ts: Optional[bytes] = await self._redis.get(self.KEY)
        if ts is None:
            return None
        return datetime.fromtimestamp(int(ts.decode('utf-8')) // 1000)
