# 0x01. Python - Async

## Description
This project covers **asynchronous programming** in Python using the `asyncio` library:
- Writing asynchronous coroutines using `async def` and `await`.
- Generating random execution delays with `asyncio.sleep()`.
- Executing multiple concurrent coroutines using `asyncio.gather()`.
- Measuring total and average execution runtime across concurrent coroutines.
- Creating and scheduling tasks with `asyncio.create_task()`.

## Tasks Summary

| File | Description |
| :--- | :--- |
| `0-basic_async_syntax.py` | Asynchronous coroutine `wait_random(max_delay: int = 10) -> float` waiting for random delay. |
| `1-concurrent_coroutines.py` | Coroutine `wait_n(n: int, max_delay: int) -> List[float]` spawning `wait_random` $n$ times concurrently and returning sorted delays. |
| `2-measure_runtime.py` | Function `measure_runtime(n: int, max_delay: int) -> float` computing total time elapsed divided by $n$. |
| `3-tasks.py` | Function `task_wait_random(max_delay: int) -> asyncio.Task` returning an event loop Task. |
| `4-tasks.py` | Modifying `wait_n` into `task_wait_n` to create tasks using `task_wait_random`. |

## Author
- **Ramy Rashad** - [GitHub](https://github.com/Ramyrashad127)
