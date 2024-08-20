"""

class Class:
  def __len__(self) -> int:
    ...

- Implements the built-in len() function

"""

class Sample:
  def __len__(self) -> int:
    return 123

sample : Sample = Sample()
print(len(sample))
# 123