"""

class ClassName:
  def __new__(cls, *args, **kwargs):
    ...
    return super(ClassName, cls).__new__(cls, *args, **kwargs)

- A static method that takes the class as its first argument
    and returns a new instance of that class

===============================================================

Parameters :

cls : class = a class to create a new instance of

*args : Optional = positional arguments

**kwargs : Optional = keyword arguments

"""

class SampleClass:
  def __new__(cls, *args, **kwargs):
    print("Creating new instance")
    return super(SampleClass, cls).__new__(cls)

  def __init__(self) -> None:
    print("__init__ is called")

sample_object : SampleClass = SampleClass()
# "Creating new instance"
# "__init__ is called"