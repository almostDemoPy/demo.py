"""

class ClassName:
  def __init__(self, other : Any) -> Any:
    ...

- Implements the built-in divmod operation

===============================================================

Parameters :

other : Any = second object

"""

class SampleClass:
  def __init__(self, number : int | float) -> None:
    self.number : int | float = number

  def __divmod__(self, other : SampleClass) -> tuple[int, int]:
    return divmod(self.number, other.number)

object_one : SampleClass = SampleClass(10)
object_two : SampleClass = SampleClass(2)
print(divmod(object_one, object_two))
# (5, 0)