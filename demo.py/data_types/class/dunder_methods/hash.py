"""

class ClassName:
  def __hash__(self) -> Any:
    ...

- Implements the built-in hash() function

"""

class SampleClass:
  def __hash__(self) -> int:
    return 13

sample_object : SampleClass = SampleClass()
print(hash(sample_object))
# 13