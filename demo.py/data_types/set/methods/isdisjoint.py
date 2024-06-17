"""

set.isdisjoint(
  set_two : set
)

- Check whether the two sets are disjoint or not. Two sets are
    disjoints when their intersection is null.

===============================================================

Parameters :

set_two : set = the second set to compare with the set

"""

set_one : set[int] = {1, 2, 3}
set_two : set[int] = {4, 5, 6}
print(set_one.isdisjoint(set_two))
# True


set_one : set[int] = {1, 2, 3}
set_two : set[int] = {3, 4, 5}
print(set_one.isdisjoint(set_two))
# False