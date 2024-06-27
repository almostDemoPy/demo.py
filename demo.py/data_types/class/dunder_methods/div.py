"""

class ClassName:
  def __div__(self, other : Any) -> float:
    ...

- Implements the floating-point division ( / )

===============================================================

Parameters :

other : Any = the second object to divide with

"""

class SampleClass:
  def __init__(self, number : int | float) -> None:
    self.number : int | float = number

  def __div__(self, other : SampleClass) -> float:
    return self.number / other.number

object_one : SampleClass = SampleClass(6)
object_two : SampleClass = SampleClass(2)
div : float = object_one / object_two
print(div)
# 3.0