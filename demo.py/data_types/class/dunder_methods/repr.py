"""

class ClassName:
  def __repr__(self) -> str:
    ...

- Returns a more information-rich, or official, string
    representation of an object

"""

class Human:
  def __init__(self, name : str) -> None:
    self.name : str = name

  def __repr__(self) -> str:
    return f"Human(name = \"{self.name}\")"

human : Human = Human("demo")
print(repr(human))
# "Human(name = "demo")"