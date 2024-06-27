"""

class ClassName:
  def __floordiv__(self, other : ...) -> ...:
    ...

- Implements the integer division operation ( // )

===============================================================

Parameters :

other : ... = the second object to floor divide with

"""

class SampleObject:
  def __init__(self, number : int | float) -> None:
    self.number : int | float = number

  def __floordiv__(self, other : SampleObject) -> int:
    return self.number // other.number

object_one : SampleObject = SampleObject(6)
object_two : SampleObject = SampleObject(2)
div : int = object_one // object_two
print(div)
# 3