#!/usr/bin/env python3
"""import modules"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """return list of floats using async generator"""
    return [x async for x in async_generator()]
