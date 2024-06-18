"""

set.symmetric_difference_update(
  set_two : Iterable
)

- Update the set with the symmetric difference of two sets

===============================================================

Parameters :

set_two : Iterable = the set to compare with

"""

set_one : set[int] = {1, 2, 3}
set_two : set[int] = {2, 3, 4}
set_one.symmetric_difference_update(set_two)
print(set_one)
# {1, 4}