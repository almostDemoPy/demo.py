"""

yield

- Used to create a generator function

"""

from random import (
  randint
)


def get_random(
  min_number : int,
  max_number : int,
  *,
  count : int = 1
) -> int:
  for i in range(count):
    yield randint(min_number, max_number)


for number in get_random(1, 5, count = 5):
  print(number)
  # 3
  # 5
  # 1
  # 5
  # 4