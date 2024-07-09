#!/usr/bin/env python3
"""Module: Async Comprehensions"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Executes async_comprehension four times in parallel using
    asyncio.gather, and measures the total runtime and then returns it.
    """
    times_on = time.time()
    await asyncio.gather(async_comprehension())
    times_up = time.time()
    total_exec_time = times_up - times_on
    return total_exec_time
