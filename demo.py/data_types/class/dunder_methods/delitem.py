"""

class Class:
  def __delitem__(self, index : Any) -> None:
    ...

- Called when the indexer operation is prefixed with
    the del-keyword

"""

class Sample:
  def __init__(self, values : list[int]) -> None:
    self.values : list[int] = values

  def __delitem__(self, index : int) -> None:
    del self.values[index]


sample : Sample = Sample([1, 2, 3])
print(sample.values)
# [1, 2, 3]
del sample[1]
print(sample.values)
# [1, 3]