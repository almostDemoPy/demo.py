"""

list.pop(
  index : Optional[int] = -1
)

- Removes elements at a specific index from the list

===============================================================

Parameters :

index : Optional[int] = the index of the element to pop out
    and remove. Defaults to the last element

"""

sample_list : list[str] = ["a", "b", "c", "d"]
sample_list.pop()
print(sample_list)
# ["a", "b", "c"]


sample_list : list[str] = ["a", "b", "c", "d"]
popped : str = sample_list.pop()
print(popped)
# "d"


sample_list : list[str] = ["a", "b", "c", "d"]
sample_list.pop(2)
print(sample_list)
# ["a", "b", "d"]