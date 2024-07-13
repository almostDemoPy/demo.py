"""

class ClassName:
  def __dir__(self) -> Any:
    ...

- Implements the functionality of the dir() built-in function.

"""

class SampleClass:
  def __init__(self, num_list : list[int]) -> None:
    self.num_list : list[int] = num_list

  def __dir__(self) -> list[int]:
    return self.num_list

sample_object : SampleClass = SampleClass([1, 2, 3])
print(dir(sample_object))
# [1, 2, 3]