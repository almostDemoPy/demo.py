"""

class Class:
  def __reversed__(self) -> Iterator:
    ...

- Called with the built-in reversed() function

"""

class Sample:
  def __init__(self, values : list[int]) -> None:
    self.values : list[int] = values

  def __reversed__(self) -> list[int]:
    return self.values[::-1]


sample : Sample = Sample([1, 2, 3])
print(sample.values)
# [1, 2, 3]
reversed_sample : list[int] = reversed(sample)
print(reversed_sample)
# [3, 2, 1]