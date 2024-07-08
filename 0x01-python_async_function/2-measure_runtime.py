#!/usr/bin/env python3
"""Module: Asynchronous coroutines"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Takes n and max_delay as args and measures the total execution time
    for wait_n(n, max_delay), and returns total_time / n.
    """
    times_on = time.time()
    asyncio.run(wait_n(n, max_delay))
    times_up = time.time()
    total_exec_time = times_up - times_on
    return total_exec_time / n
