#!/usr/bin/env python3
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    wait_coroutine = wait_random(max_delay)

    wait_task = asyncio.create_task(wait_coroutine)
    
    return wait_task