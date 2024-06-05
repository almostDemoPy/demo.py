"""

list.count(
  element : Any
)

- Returns the count of the occurences of a given element in a
    list

==============================================================

Parameters :

element : Any = the item whose count is to be returned

"""

sample_list : list = [
  1, 2, 3, 5, 1, 2, 4, 3, 1, 5, 1, 2
]
print(sample_list.count(1))
# 4