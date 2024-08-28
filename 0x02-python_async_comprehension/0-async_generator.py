#!/usr/bin/env python3
"""import modules"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """async generator for integers numbers"""
    for i in range(10):
        await asyncio.sleep(1)
        v = random.uniform(0, 10)
        yield v
