"""

class ClassName:
  def __mod__(self, other : Any) -> Any:
    ...

- Implements the modulo operation ( % )

===============================================================

Parameters :

other : Any = second object to get the remainder with

"""

class SampleClass:
  def __init__(self, number : int | float) -> None:
    self.number : int | float = number

  def __mod__(self, other : SampleClass) -> int | float:
    return self.number % other.number

object_one : SampleClass = SampleClass(5)
object_two : SampleCLass = SampleClass(2)
print(object_one % object_two)
# 1