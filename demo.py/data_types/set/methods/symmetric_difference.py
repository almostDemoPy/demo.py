"""

set.symmetric_difference(
  set_two : set
)

- Return a new set with the elements that are in either sets
    but not in both

===============================================================

Parameters :

set_two : set = the second set to compare with

"""

set_one : set[int] = {1, 2, 3}
set_two : set[int] = {2, 3, 4}
print(set_one.symmetric_difference(set_two))
# {1, 4}