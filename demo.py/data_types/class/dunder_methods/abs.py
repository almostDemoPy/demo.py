"""

class ClassName:
  def __abs__(self) -> int | float:
    ...

- Called when the built-in abs() function is applied to an
    instance of the class

"""

class SampleClass:
  def __init__(self, number : int | float) -> None:
    self.number : int | float = number

  def __abs__(self) -> int | float:
    return abs(self.number)

sample_object : SampleClass = SampleClass(-13)
print(abs(sample_object))
# 13