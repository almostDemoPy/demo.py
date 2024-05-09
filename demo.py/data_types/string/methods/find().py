"""

str.find(
  substring : str,
  start : Optional[int],
  end : Optional[int]
)

- Return the lowest index of the specified substring if found, otherwise returns -1

Parameters :
  substring : str = the substring to look for
  start : Optional[int] = starting position of the search
  end : Optional[int] = ending position of the search

"""

string : str = "sample string"

print(string.find("ple"))
# 3

print(string.find("e", 3))
# 5

print(string.find("hello"))
# -1