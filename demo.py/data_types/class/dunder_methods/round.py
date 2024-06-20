"""

class ClassName:
  def __round__(self, ndigits : int = 0) -> int | float:
    ...

- Implements the built-in round() function

===============================================================

ndigits : int = round the number to this given precision.
    Defaults to 0.

"""

class SampleClass:
  def __init__(self, number : int | float) -> None:
    self.number : int | float = number

  def __round__(self, ndigits : int = 0) -> int:
    return round(self.number, ndigits = ndigits)

sample_object : SampleClass = SampleClass(12.34)
print(round(sample_object))
# 12


print(round(sample_object, ndigits = 1))
# 12.3


# Case : negative ndigits

print(round(sample_object, ndigits = -1))
# 10