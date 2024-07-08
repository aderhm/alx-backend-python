#!/usr/bin/env python3
"""Module: Asynchronous coroutine"""

import asyncio
from asyncio.tasks import Task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """Creates an asyncio.Task from wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
