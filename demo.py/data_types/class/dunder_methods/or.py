"""

class ClassName:
  def __or__(self, other : Any) -> Any:
    ...

- Implements the built-in Bitwise OR | operation

===============================================================

Parameters :

other : Any = other value

"""

from typing import Self

class SampleClass:
  def __init__(self, number : int) -> None:
    self.number : int = number

  def __or__(self, other : Self) -> int:
    return self.number | other.number

object_one : SampleClass[int] = SampleClass(32)
object_two : SampleClass[int] = SampleClass(16)
print(object_one | object_two)
# 48