"""

class Class:
  def __complex__(self) -> complex:
    ...

- Implements the built-in complex() function

"""

class Sample:
  def __complex__(self) -> complex:
    return 3+1j

sample : Sample = Sample()
print(complex(sample))
# (3+1j)