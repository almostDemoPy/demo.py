"""

class ClassName:
  def __lshift__(self, other : Any) -> Any:
    ...

- Implements the built-in << operation

===============================================================

Parameters :

other : Any = other object / data

"""

class SampleClass:
  def __init__(self, number : int) -> None:
    self.number : int = number

  def __lshift__(self, other : int) -> int:
    return self.number << other.number

object_one : SampleClass[int] = SampleClass(8)
object_two : SampleClass[int] = SampleClass(1)
print(object_one << object_two)
# 16