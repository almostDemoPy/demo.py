"""

class ClassName:
  def __str__(self) -> str:
    ...

- Returns a human-readable, or informal, string representation
    of an object

"""

class Human:
  def __init__(self, name : str) -> None:
    self.name : str = name

  def __str__(self) -> str:
    return self.name

huma : Human = Human("demo")
print(str(human))
# "demo"