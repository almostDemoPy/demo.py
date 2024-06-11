"""

set.discard(
  element : Union[int, bool, str, float]
)

- Remove an element from the set

===============================================================

Parameters :

element : Union[int, bool, str, float] = the element to remove
    from the set

"""

sample_set : set[int] = {1, 2, 3}
sample_set.discard(2)
print(sample_set)
# {1, 3}