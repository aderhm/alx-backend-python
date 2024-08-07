#!/usr/bin/env python3
"""Module: Async Comprehension"""

import asyncio
import typing

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """Collects 10 random numbers using an async comprehensing over
    async_generator, then return the 10 random numbers.
    """
    return [n async for n in async_generator()]
