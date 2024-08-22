"""

class Class:
  def __setattr__(self, name : str, value : Any) -> None:
    ...

- Called when setting a value to an attribute

"""

class Sample:
  def __setattr__(self, name : str, value : int) -> None:
    self.__dict__[name] = value

sample : Sample = Sample()
sample.number : int | float = 123
print(sample.number)
# 123