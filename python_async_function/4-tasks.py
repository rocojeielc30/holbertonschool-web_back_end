#!/usr/bin/env python3 
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    running_tasks = []
    for _ in range(n):
        running_tasks.append(task_wait_random(max_delay))

    finished_delays = []
    for next_finished_task in asyncio.as_completed(running_tasks):
        delay = await next_finished_task
        finished_delays.append(delay)

    return finished_delays