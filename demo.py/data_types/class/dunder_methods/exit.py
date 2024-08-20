"""

class Class:
  def __exit__(self) -> Any:
    ...

- Called when the with-as block is done processing

"""

class Sample:
  def __enter__(self) -> None:
    print("ctx manager entered")

  def __exit__(self) -> None:
    print("ctx manager exited")

with Sample() as sample:
  # "ctx manager entered"
  print("hello world")
  # "hello world"
# "ctx manager exited"