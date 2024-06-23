"""

class ClassName:
  def __neg__(self) -> Any:
    pass

- Negate a custom object

"""

class SampleClass:
  def __init__(self, number : int | float) -> None:
    self.number : int | float = number

  def __neg__(self) -> int | float:
    return self.number * -1

sample_object : SampleClass = SampleClass(123)
print(-sample_object)
# -123