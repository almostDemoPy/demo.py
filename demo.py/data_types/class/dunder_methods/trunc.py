"""

class ClassName:
  def __trunc__(self) -> int:
    ...

- Implements the behavior of the math.trunc() function

"""

import math

class SampleClass:
  def __init__(self, number : int) -> None:
    self.number : int = number

  def __trunc__(self) -> int:
    return 10

sample_object : SampleClass = SampleClass(99)
print(math.trunc(sample_object))
# 10