#!/usr/bin/env python3
"""import modules"""
import asyncio
import time
wait_n = __import__('2-measure_runtime.py').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """new function for python"""
    st = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - st
    return total_time / n
