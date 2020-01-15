# pylint: disable=too-few-public-methods

import os

import asyncpg.pool as apg_pool
import asyncpg

from lms.settings import POSTGRES_CONNECTION_CONF


class AsyncPool:
    def __init__(self):
        self.pool = None

    async def get_pool(self) -> apg_pool.Pool:
        if not self.pool:
            self.pool = await self._create_pool()
        return self.pool

    @staticmethod
    async def _create_pool() -> apg_pool.Pool:
        conf = POSTGRES_CONNECTION_CONF
        if os.environ.get('postgres_host', default=None):
            conf['host'] = os.environ.get('postgres_host')
            print('using postgres host from ENV: ', conf['host'])
        return await asyncpg.create_pool(**POSTGRES_CONNECTION_CONF)


_POOL = AsyncPool()


async def get_pool() -> apg_pool.Pool:
    return await _POOL.get_pool()
