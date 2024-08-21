"""

class Class:
  def __call__(self, *args, **kwrags) -> Any:
    ...

- Called when the class is called like a function

"""

class Sample:
  def __call__(self, string : str) -> None:
    print(string)

Sample("hello world")