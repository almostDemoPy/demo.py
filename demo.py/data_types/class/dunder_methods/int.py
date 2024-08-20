"""

class Class:
  def __int__(self) -> int:
    ...

- Implements the built-in int() function

"""

class Sample:
  def __int__(self) -> int:
    return 42


sample : Sample = Sample()
print(int(sample))
# 42