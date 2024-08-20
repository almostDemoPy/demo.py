"""

class Class:
  def __bool__(self) -> bool:
    ...

- Implements the built-in bool() function

"""

class Sample:
  def __bool__(self) -> bool:
    return True

sample : Sample = Sample()
print(bool(sample))
# True