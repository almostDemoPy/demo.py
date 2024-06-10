"""

set.add(
  element : Any
)

- Adds an element to the set if it is not present in the set
    yet

===============================================================

Parameters :

element : Any = the element to add in the list

"""

sample_set : set[int] = {}
sample_set.add(1)
print(sample_set)
# {1}


# Case : element already exists in set

sample_set : set[int] = {1}
sample_set.add(1)
print(sample_set)
# {1}