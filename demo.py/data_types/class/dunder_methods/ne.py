"""

class ClassName:
  def __ne__(self, other : Any) -> bool:
    ...

- Customizes the behavior of the non-equality operator

===============================================================

Parameters :

other : Any = other object / data

"""

from typing import Self

class Sample:
  def __init__(self, number : int) -> None:
    self.number : int = number

  def __ne__(self, other : Self) -> bool:
    return self.number != other.number

sample_one : Sample = Sample(2)
sample_two : Sample = Sample(2)
print(sample_one != sample_two)
# False