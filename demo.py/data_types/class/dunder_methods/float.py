"""

class Class:
  def __float__(self) -> float:
    ...

- Implements the built-in float() function

"""

class Sample:
  def __float__(self) -> float:
    return 42.3

sample : Sample = Sample()
print(float(sample))
# 42.3