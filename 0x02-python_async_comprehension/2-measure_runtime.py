#!/usr/bin/env python3
"""import modules"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measure for the time"""
    start = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(), async_comprehension(), async_comprehension()
    )
    end = time.time()
    return end - start
