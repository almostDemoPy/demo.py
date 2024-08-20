"""

class Class:
  def __getitem__(self, items : Any) -> Any:
    ...

-  Called with the indexer [] operation

"""

class Sample:
  def __getitem__(self, slot : int) -> int:
    return slot

sample : Sample = Sample()
print(sample[23])
# 23