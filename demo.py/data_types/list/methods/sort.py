"""

list.sort(
  reverse : Optional[bool] = False,
  key : Optional[Callable] = None
)

- Sorts the elements of a list in ascending or descending
    order

===============================================================

Parameters :

reverse : Optional[bool] = whether to sort the list in
    descending order. Defaults to False

key : Optional[Callabale] = A function to specify the sorting
    criteria(s)

"""

sample_list : list[int] = [1, 2, 1, 8, 3, 8, 4, 3, 8, 1, 8]
sample_list.sort()
print(sample_list)
# [1, 1, 1, 2, 3, 3, 4, 8, 8, 8, 8]


sample_list : list[int] = [8, 2, 8, 1, 9, 2, 7, 4, 2, 9, 2]
sample_list.sort(reverse = True)
print(sample_list)
# [9, 9, 8, 8, 7, 4, 2, 2, 2, 2, 1]


# Case : providing own method

def even_sort(value : int) -> int:
  return value[1]

sample_list : list[tuple[int]] = [(1, 2), (3, 6), (4, 5)]
sample_list.sort(key = even_sort)
print(sample_list)
# [(1, 2), (4, 5), (3, 6)]