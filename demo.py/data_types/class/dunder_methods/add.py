"""

class ClassName:
  def __add__(self, other : Any) -> Any:
    ...

- Returns a new third object from the addition of 2 other
    objects with the addition operator

===============================================================

Parameters :

other : Any = Second object to add in the first object

"""

class SampleClass:
  def __init__(self, text : str) -> None:
    self.text : str = text

  def __add__(self, other : str) -> SampleClass:
    return SampleClass(self.text + " " + other.text)

object_one : SampleClass = SampleClass("Simple")
object_two : SampleClass = SampleClass("Python")
object_three : SampleClass = object_one + object_two
print(object_three.text)
# "Simple Python"