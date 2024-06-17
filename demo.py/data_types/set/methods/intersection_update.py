"""

set.intersection_update(
  sets : set,
  ...
)

- Update the set with the common elements of all the sets

===============================================================

Parameters :

sets : set = the sets to get the common elements of and update
    the set with

"""

set_one : set[int] = {1, 2, 3}
set_two : set[int] = {2, 3, 4}
set_one.intersection_update(set_two)
print(set_one)
# {2, 3}