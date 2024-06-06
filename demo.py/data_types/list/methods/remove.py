"""

list.remove(
  element : Any
)

- Removes a given element

===============================================================

Parameters :

element : Any = the element to remove

"""

sample_list : list[str] = ["a", "b", "c", "d"]
sample_list.remove("a")
print(sample_list)
# ["b", "c", "d"]


# Case : duplicates of elements in the list

sample_list : list[int] = [1, 2, 3, 5, 2, 4, 3, 6]
sample_list.remove(2)
print(sample_list)
# [1, 3, 5, 2, 4, 3, 6]