"""

class ClassName:
  def __sub__(self, other : Any) -> Any:
    ...

- Returns a new object that represents the difference of two
    objects

===============================================================

Parameters :

other : Any = Second object to deduct from the first object

"""

class SampleClass:
  def __init__(self, number : int | float) -> None:
    self.number : int | float = number

  def __sub__(self, other : int | float) -> int | float:
    return SampleClass(self.number - other.number)

object_one : SampleClass = SampleClass(100)
object_two : SampleClass = SampleClass(33)
object_three : SampleClass = object_one - object_two
print(object_three.number)
# 67