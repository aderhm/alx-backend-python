#!/usr/bin/env python3
"""Module: Asynchronous coroutine"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Takes in 2 int args: n and max_delay, spawns wait_random n times
    with the specified max_delay, returns the list of all the delays
    """
    delays = await asyncio.gather(
        *[task_wait_random(max_delay) for _ in range(n)])

    return sorted(delays)
