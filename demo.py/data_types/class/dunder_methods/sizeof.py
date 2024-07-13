"""

class ClassName:
  def __sizeof__(self) -> int:
    ...

- Returns the size of the object in bytes

"""

class SampleClass:
  def __sizeof__(self) -> int:
    return 13

sample_object : SampleClass = SampleClass()
print(sample_object.__sizeof__())
# 13