#!/usr/bin/env python3
import asyncio
import random
from typing import Generator

async def async_generator() -> Generator[float, None, None]:
    number_of_loops = 10 
    wait_seconds = 1

    for _ in range(number_of_loops):
        await asyncio.sleep(wait_seconds)
        random_number = random.uniform(0,10)
        yield random_number