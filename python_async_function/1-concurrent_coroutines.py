#!/usr/bin/env python3
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    running_waits = []
    for _ in range(n):
        running_waits.append(wait_random(max_delay))

    finished_delays = []
    for next_finished_wait in asyncio.as_completed(running_waits):
        delay = await next_finished_wait
        finished_delays.append(delay)

    return finished_delays
