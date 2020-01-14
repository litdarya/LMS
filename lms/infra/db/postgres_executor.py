from typing import Tuple, Any, List, Optional
import asyncpg
from lms.infra.db.async_pool import get_pool


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
) -> Optional[Any]:
    pool = await get_pool()
    async with pool.acquire() as connection:
        return await connection.fetchval(query, *params)


async def fetch_row(
        *,
        query: str,
        params: Optional[Tuple[Any, ...]] = tuple()
) -> asyncpg.Record:
    pool = await get_pool()
    async with pool.acquire() as connection:
        return await connection.fetchrow(query, *params)
