"""

class ClassName:
  def __del__(self) -> None:
    ...

- Called as soon as all references of the object are deleted
    i.e when an object is garbage collected

"""

class SampleClass:
  def __del__(self) -> None:
    print("object deleted")

sample_object : SampleClass = SampleClass()
del sample_object
# "object deleted"