"""

class Class:
  def __iter__(self) -> Iterator:
    ...

- Called with the built-in iter() function or in a
    for-loop

"""

from typing import Self

class Sample:
  def __init__(self, values : list[str]) -> None:
    self.values : list[str] = values
    self.current : int | None = values[0] if values else None

  def __iter__(self) -> Self:
    return self

  def __next__(self) -> int | None:
    if self.current is None: return None
    self.current += 1
    return self.current - 1

sample : Sample = Sample()
sample_iterator = iter(sample)
print(next(sample_iterator))
# None
sample : Sample = Sample([1, 2, 3])
sample_iterator = iter(sample)
print(next(sample_iterator))
# 1
print(next(sample_iterator))
# 2