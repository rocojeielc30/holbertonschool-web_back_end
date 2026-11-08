#!/usr/bin/env python3
"""An async generator that yields 10 random numbers, one per second."""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Wait 1 second, then yield a random number from 0 to 10, 10 times."""
    number_of_loops = 10
    wait_seconds = 1

    for _ in range(number_of_loops):
        await asyncio.sleep(wait_seconds)

        random_number = random.uniform(0, 10)
        yield random_number
