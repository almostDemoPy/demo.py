"""

class Class:
  def __getattr__(self, attribute) -> Any:
    ...

- Called when it failed to access an attribute

"""

class Sample(object):
  def __init__(self) -> None:
    self.number : int | float = 2

  def __getattribute(self, attribute) -> int:
    return super(Sample, self).__getattribute__(attribute)

  def __getattr__(self, attribute) -> None:
    print(f"Attribute {attribute} not found")

sample : Sample = Sample()
print(sample.name)
# "Attribute name not found"