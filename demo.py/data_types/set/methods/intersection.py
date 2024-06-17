"""

set.intersection(
  sets : set,
  ...
)

- Return a new set with elements that are common to all set

===============================================================

Parameters :

sets : set = sets to retrieve the common elements of

"""

set_one : set[int] = {1, 2, 3}
set_two : set[int] = {2, 3, 4}
print(set_one.intersection(set_two))
# {2, 3}


set_one : set[int] = {1, 2, 3}
set_two : set[int] = {2, 3, 4}
set_three : set[int] = {3, 4, 5}
print(set_one.intersection(set_two, set_three))
# {3}