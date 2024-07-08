#!/usr/bin/env python3
"""Module: Asynchronous coroutine
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Takes in 2 int args: n and max_delay, spawns wait_random n times
    with the specified max_delay, returns the list of all the delays
    """
    delays = []
    for _ in range(n):
        delays.append(await wait_random(max_delay))
    return sorted(delays)
