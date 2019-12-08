from typing import Tuple, Any, List, Optional

import asyncpg
import asyncpg.pool as apg_pool

from lms.settings import POSTGRES_CONNECTION_CONF


async def create_pool() -> apg_pool.Pool:
    return await asyncpg.create_pool(**POSTGRES_CONNECTION_CONF)


_pool = None


async def get_pool() -> apg_pool.Pool:
    global _pool
    if _pool is None:
        _pool = await create_pool()
    return _pool


async def fetch(
        *,
        query: str,
        params: Optional[Tuple[Any, ...]] = tuple()
) -> List[asyncpg.Record]:
    pool = await get_pool()
    async with pool.acquire() as connection:
        return await connection.fetch(query, *params)


async def fetch_val(
        *,
        query: str,
        params: Optional[Tuple[Any, ...]] = tuple()
) -> asyncpg.Record:
    pool = await get_pool()
    async with pool.acquire() as connection:
        return await connection.fetchval(query, *params)
