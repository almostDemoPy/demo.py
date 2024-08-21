"""

class Class:
  def __next__(self) -> Any:
    ...

- Called with the built-in next() function

"""

class Sample:
  def __init__(self, values : list[int]) -> None:
    self.values : list[int] = values
    self.current : int = 0

  def __next__(self) -> int:
    self.current += 1
    return self.values[self.current - 1]

sample : Sample = Sample([1, 2, 3])
print(next(sample))
# 1
print(next(sample))
# 2