"""

class ClassName:
  def __gt__(self, other : Any) -> bool:
    ...

- Customize the behavior of the greater-than operator

===============================================================

Parameters :

other : Any = other object / data

"""

from typing import Self

class Sample:
  def __init__(self, number : int) -> None:
    self.number : int = number

  def __gt__(self, other : Self) -> bool:
    return self.number > other.number

sample_one : Sample = Sample(1)
sample_two : Sample = Sample(2)
print(sample_one > sample_two)
# False