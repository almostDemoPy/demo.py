"""

class ClassName:
  def __init__(self, *args, **kwargs) -> None:
    ...

- Initialize objects of a class

"""

class SampleClass:
  def __init__(self) -> None:
    print("__init__ called")

sample : SampleClass = SampleClass()
# "__init__ called"