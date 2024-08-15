"""

nonlocal

- Used to reference a variable on the nearest
    scope

"""

def foo() -> str:
  string : str = "hello"

  def bar() -> None:
    nonlocal string
    string = "world"

  bar()
  return string

print(foo())
# "world"


# ===========================================

def foo() -> str:
  string : str = "hello"

  def bar() -> None:
    string : str = "world"

    def hoo() -> None:
      nonlocal string
      print(string)
      # "world"
      string = "python"
      print(string)
      # "python"

    hoo()

  bar()
  return string

print(foo())
# "hello"