"""

class ClassName:
  def __pos__(self) -> Any:
    ...

- Called to implement the unary + arithmetic operation

"""

class SampleClass:
  def __init__(self, number : int | float) -> None:
    self.number : int | float = number

  def __pos__(self) -> int | float:
    return abs(self.number)

sample_object : SampleClass = SampleClass(-123)
print(+sample_object)
# 123