"""

class ClassName:
  def __format__(self, specifier : Any) -> Any:
    ...

- Implements the built-in format() function

===============================================================

Parameters :

specifier : Any = the format specifier value

"""

class System:
  def __format__(self, specifier : str) -> str:
    return f"hello {specifier}"

system : System = System()
print(format(system, "world"))
# "hello world"