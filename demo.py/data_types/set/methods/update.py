"""

set.update(
  set_two : set
)

- Add elements to the set

===============================================================

Parameters :

set_two : set = the set containing the elements to add to the
    original set

"""

set_one : set[int] = {1, 2, 3}
set_two : set[int] = {3, 4, 5}
set_one.update(set_two)
print(set_one)
# {1, 2, 3, 4, 5}