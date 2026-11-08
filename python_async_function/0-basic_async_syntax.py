#!/usr/bin/env python3

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    shortest_delay = 0
    longest_delay = max_delay
    delay = random.uniform(shortest_delay, longest_delay)

    await asyncio.sleep(delay)
    return delay
    