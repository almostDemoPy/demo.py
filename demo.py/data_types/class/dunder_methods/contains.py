"""

class Class:
  def __contains__(self, value : Any) -> bool:
    ...

- Called with the in-keyword

"""

class Sample:
  def __init__(self, values : list[int]) -> None:
    self.values : list[int] = values

  def __contains__(self, value : int) -> bool:
    return value in self.values


sample : Sample = Sample([1, 2, 3])
print(2 in sample)
# True