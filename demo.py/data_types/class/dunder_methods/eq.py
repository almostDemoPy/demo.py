"""

class ClassName:
  def __eq__(self, other : Any) -> bool:
    ...

- Customizes the behavior of the equality operator

===============================================================

Parameters :

other : Any = second object / data

"""

from typing import Self

class Sample:
  def __init__(self, number : int) -> None:
    self.number : int = number

  def __eq__(self, other : Self) -> bool:
    return self.number == other.number

sample_one : Sample = Sample(2)
sample_two : Sample = Sample(3)
print(sample_one == sample_two)
# False