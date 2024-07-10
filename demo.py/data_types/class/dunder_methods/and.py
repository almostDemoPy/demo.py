"""

class ClassName:
  def __and__(self, other : Any) -> Any:
    ...

- Implements the built-in & operator

===============================================================

Parameters :

other : Any = other object / data

"""

class SampleClass:
  def __init__(self, number : int) -> None:
    self.number : int = number

  def __and__(self, other : int) -> None:
    return self.number & other.number

object_one : SampleClass[int] = SampleClass(10)
object_two : SampleClass[int] = SampleClass(4)
print(object_two & object_three)
# 0