"""

list.index(
  element : Any,
  start : Optional[int] = 0,
  end : Optional[int] = -1
)

- Returns the index of the first occurence of the item

===============================================================

Parameters :

element : Any = the element to look for

start : Optional[int] = starting index of search

end : Optional[int] = ending position of search

"""

sample_list : list[int] = [1, 2, 3, 4, 5]
print(sample_list.index(3))
# 2


sample_list : list[str] = ["a", "b", "c", "d", "e"]
print(sample_list.index("a"))
# 0


# Case : element is not present in list

sample_list : list[str] = ["a", "b", "c"]
print(sample_list.index("d"))
# ValueError: "d" is not in list