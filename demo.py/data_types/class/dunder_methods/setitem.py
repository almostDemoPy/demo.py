"""

class Class:
  def __setitem__(self, index : Any, value : Any) -> None:
    ...

- Called when setting a value with the indexer []
    operation

"""

class Sample:
  def __init__(self, values : list[int]) -> None:
    self.values : list[int] = values

  def __getitem__(self, slot : int) -> int:
    return self.values[slot - 1]

  def __setitem__(self, slot : int, value : int) -> None:
    self.values[slot - 1] = value

sample : Sample = Sample([1, 2, 3])
print(sample[2])
# 2
sample[2] = 4
print(sample[2])
# 4