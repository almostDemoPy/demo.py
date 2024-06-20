"""

class ClassName:
  def __invert__(self) -> int | float:
    ...

- Used to define the behavior of the bitwise NOT operator ( ~ )

"""

class SampleClass:
  def __init__(self, number : int | float) -> None:
    self.number : int | float = number

  def __invert__(self) -> int | float:
    return SampleClass(~self.number)

sample_object : SampleClass = SampleClass(13)
inverted_sample_object = ~sample_object
print(inverted_sample_object.number)
# -14