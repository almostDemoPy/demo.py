"""

set.remove(
  element : Any
)

- Remove an element from the set

===============================================================

Parameters :

element : Any = the element to remove from the set

"""

sample_set : set[int] = {1, 2, 3}
sample_set.remove(2)
print(sample_set)