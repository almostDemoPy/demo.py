"""

set.union(
  sets : set,
  ...
)

- Return a new set that contains all the items from all the
    original sets

===============================================================

Parameters :

sets : set = the sets to compare with

"""

set_one : set[int] = {1, 2, 3}
set_two : set[int] = {2, 3, 4}
print(set_one.union(set_two))
# {1, 2, 3, 4}