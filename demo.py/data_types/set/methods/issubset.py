"""

set.issubset(
  set_two : set
)

- Check if all elements in set A are present in set B

===============================================================

Parameters :

set_two : set = the second set to compare the set with

"""

set_one : set[int] = {1, 2, 3, 4, 5}
set_two : set[int] = {2, 4}
print(set_two.issubset(set_one))
# True


set_one : set[int] = {2, 4}
set_two : set[int] = {1, 2, 3, 4, 5}
print(set_two.issubset(set_one))
# False