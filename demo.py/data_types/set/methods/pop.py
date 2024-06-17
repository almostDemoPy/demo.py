"""

set.pop()

- Removes and returns any random element from the set

"""

sample_set : set[int] = {1, 2, 3}
removed : int = sample_set.pop()
print(sample_set)
# {1, 3}
print(removed)
# 2