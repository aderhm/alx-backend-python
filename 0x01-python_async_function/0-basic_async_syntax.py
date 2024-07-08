#!/usr/bin/env python3
"""Module: Practice async basics
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a random delay between 0 and max_delay seconds
    and eventually returns it
    """
    rtw = random.uniform(0, max_delay)
    await asyncio.sleep(random.uniform(0, rtw))
    return rtw
