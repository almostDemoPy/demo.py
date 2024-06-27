"""

class ClassName:
  def __truediv__(self, other : Any) -> float:
    ...

- Implements the normal division operation ( / )

===============================================================

Parameters :

other : Any = second object to normal divide with

"""

class SampleClass:
  def __init__(self, number : int | float) -> None:
    self.number : int | float = number

  def __truediv__(self, other : SampleClass) -> float:
    return self.number / other.number

object_one : SampleClass = SampleClass(6)
object_two : SampleClass = SampleClass(3)
print(object_one / object_two)
# 2.0