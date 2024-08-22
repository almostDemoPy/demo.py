"""

class Class:
  def __delattr__(self, name : str) -> None:
    ...

- Called when there is an attempt of deleting an
    attribute

"""

class Sample:
  def __setattr__(self, name : str, value : int) -> None:
    self.__dict__[name] = value

  def __delattr__(self, name : str) -> None:
    del self.__dict__[name]


sample : Sample = Sample()
sample.number : int | float = 123
print(sample.number)
# 123
del sample.number
print(sample.number)
# AttributeError