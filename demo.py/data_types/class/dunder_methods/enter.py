"""

class Class:
  def __enter__(self) -> Any:
    ...

- Returns a value given to the as-keyword when used
    with the with-keyword

"""

class Sample:
  def __enter__(self) -> None:
    print("context manager entered")

with Sample() as sample:
  # "context manager entered"
  print("hello world")
  # "hello world"