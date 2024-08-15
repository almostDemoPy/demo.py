"""

async

- Used to construct an asynchronous function
    or context manager

"""


from asyncio import (
  run
)


async def function() -> None:
  print(True)
  # True

run(function())