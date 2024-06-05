"""

list.append(
  element : Any
)

- Add elements at the end of the list

===============================================================

Parameters :

element : Any = the element to be added at the end of the list

"""

sample_list : list = []
sample_list.append("a")
print(sample_list)
# ["a"]


sample_list.append(1)
print(sample_list)
# ["a", 1]


sample_list.append([1, 2, 3])
print(sample_list)
# ["a", 1, [1, 2, 3]]