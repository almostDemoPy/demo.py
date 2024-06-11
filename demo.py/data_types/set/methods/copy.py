"""

set.copy()

- Create a shallow copy of the set

"""

set_one : set[int] = {1, 2, 3}
set_two : set[int] = set_one.copy()
print(set_one == set_two)
# True