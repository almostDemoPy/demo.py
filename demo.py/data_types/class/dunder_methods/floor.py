"""

class ClassName:
  def __floor__(self) -> int:
    ...

- Implements the behavior of the math.floor() function

"""

import math

class SampleClass:
  def __init__(self, number : int | float) -> None:
    self.number : int | float = None

  def __floor__(self) -> int:
    return int(self.number)

sample_object : SampleClass = SampleClass(12.34)
print(math.floor(sample_object))
# 12