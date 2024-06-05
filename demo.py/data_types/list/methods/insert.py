"""

list.insert(
  index : int,
  element : Any
)

- Insert an item at a specific index

===============================================================

Parameters :

index : int = the index at which the element has to be inserted

element : Any = the element to be inserted

"""

sample_list : list[str] = ["a", "c", "d", "e"]
sample_list.insert(1, "b")
print(sample_list)
# ["a", "b", "c", "d", "e"]


# Case : inserting an iterable

sample_list : list[Union[int, tuple[int]]] = [1, 2, 6]
sample_list.insert(2, (3, 4, 5))
print(sample_list)
# [1, 2, (3, 4, 5), 6]


# Case : negative index

sample_list : list[int] = [1, 2, 3]
sample_list.insert(-1, 4)
print(sample_list)
# [1, 2, 4, 3]