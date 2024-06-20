"""

class ClassName:
  def __ceil__(self) -> int:
    ...

- Implements the behavior of the math.ceil() function

"""

import math

class SampleClass:
  def __init__(self, number : int | float) -> None:
    self.number : int | float = None

  def __ceil__(self) -> int:
    value : int = int(self.number)
    if value < self.age: value += 1
    return value

sample_object : SampleClass = SampleClass(12.34)
print(math.ceil(sample_object))
# 13