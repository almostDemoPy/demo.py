"""

set.difference(
  second_set : set
)

- Return a set that is the difference between two sets

===============================================================

Parameters :

seccond_set : set = the set to compare the initial set to

"""

set_one : set[int] = {1, 2, 3}
set_two : set[int] = {2, 4, 6}
print(set_one.difference(set_two))
# {1, 3}