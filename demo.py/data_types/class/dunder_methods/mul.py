"""

class ClassName:
  def __mul__(self, other : Any) -> Any:
    ...

- Called to implement the arithmetic * multiplication operation

===============================================================

Parameters :

other : Any = second object to multiple to the first object

"""

class SampleClass:
  def __init__(self, number : int | float) -> None:
    self.number : int | float = number

  def __mul__(self, other : int | float) -> int | float:
    return SampleClass(self.number * other.number)

object_one : SampleClass = SampleClass(3)
object_two : SampleClass = SampleClass(4)
object_three : SampleClass = object_one * object_two
print(object_three.number)
# 12