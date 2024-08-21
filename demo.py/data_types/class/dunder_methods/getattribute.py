"""

class Class:
  def __getattribute__(self, attribute) -> Any:
    ...

- Called when trying to access an attribute

"""

class Sample(object):
  def __init__(self) -> None:
    self.number : int | float = 2

  def __getattribute__(self, attribute):
    return super(Sample, self).__getattribute__(attribute)

sample : Sample = Sample()
print(sample.number)
# 2