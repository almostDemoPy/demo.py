"""

class ClassName:
  def __pow__(self, other : Any) -> Any:
    ...

- Implements the built-in exponentiation operation

===============================================================

Parameters :

other : Any = the other object / data

"""

class SampleClass:
  def __init__(self, number : int | float) -> None:
    self.number : int | float = None

  def __pow__(self, other : int | float) -> int | float:
    return self.number ** other.number

object_one : SampleClass[int] = SampleClass(2)
object_two : SampleClass[int] = SampleClass(3)
print(object_one ** object_two)
# 8