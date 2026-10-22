# 0x02. Python - Async Comprehension

## Description
This project focuses on advanced asynchronous Python patterns: **Asynchronous Generators** and **Asynchronous Comprehensions**:
- Building asynchronous generator functions yielding numbers asynchronously (`yield`).
- Using asynchronous list comprehensions syntax: `[i async for i in async_generator()]`.
- Running multiple async comprehensions concurrently and analyzing runtime characteristics.

## Tasks Summary

| File | Description |
| :--- | :--- |
| `0-async_generator.py` | Coroutine `async_generator()` looping 10 times, asynchronously waiting 1 second, and yielding random float between 0 and 10. |
| `1-async_comprehension.py` | Coroutine `async_comprehension() -> List[float]` collecting 10 random numbers using an async comprehension over `async_generator`. |
| `2-measure_runtime.py` | Coroutine `measure_runtime() -> float` executing `async_comprehension` four times in parallel using `asyncio.gather` and measuring total runtime (~10 seconds). |

## Author
- **Ramy Rashad** - [GitHub](https://github.com/Ramyrashad127)
