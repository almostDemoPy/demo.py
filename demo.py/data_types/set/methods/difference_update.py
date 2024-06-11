"""

set.difference_update(
  second_set : int
)

- Return the difference of 2 sets and update the set with the
    difference

===============================================================

Parameters :

second_set : set = the set to compare the initial set to

"""

set_one : set[int] = {1, 2, 3}
set_two : set[int] = {2, 4, 6}
set_one.difference_update(set_two)
print(set_one)
# {1, 3}