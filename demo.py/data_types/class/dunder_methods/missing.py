"""

class Class:
  def __missing__(self, key : Any) -> None:
    ...

- Called when a non-existent key was attempted to be
    accessed

"""

class Sample:
  def __init__(self, data : dict[int, str]) -> None:
    self.data : dict[int, str] = data

  def __missing__(self, key : int) -> None:
    print(f"Key '{key}' does not exist in the data")

sample : Sample = Sample({1 : "one", 2 : "two"})
print(sample[3])
# "Key '3' does not exist in the data"