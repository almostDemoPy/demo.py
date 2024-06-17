"""

set.issuperset(
  set_b : set
)

- Check if all elements of set B are in set A

===============================================================

Parameters :

set_b : set = the second set to compare with

"""

set_one : set[int] = {1, 2, 3, 4, 5}
set_two : set[int] = {2, 4}
print(set_one.issuperset(set_two))
# True


set_one : set[int] = {2, 4}
set_two : set[int] = {1, 2, 3, 4, 5}
print(set_one.issuperset(set_two))
# False