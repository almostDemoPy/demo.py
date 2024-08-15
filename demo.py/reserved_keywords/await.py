"""

await

- Used to call an asynchronous function

"""


from asyncio import (
  run
)

async def function() -> None:
  print(True)
  # True


async def main() -> None:
  await function()


run(main())