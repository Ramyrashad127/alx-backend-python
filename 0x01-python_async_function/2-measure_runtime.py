#!/usr/bin/env python3
"""import modules"""
import asyncio
import time
wait_n = __import__('2-measure_runtime.py').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Waits for delays"""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    total = time.time() - start
    return total / n
