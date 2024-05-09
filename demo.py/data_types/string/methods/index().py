"""

str.index(
  substring : str,
  start : Optional[int] = 0,
  end : Optional[int] = 0
)

- Return the index of the first occurence of the provided substring

Parameters :
  substring : str = the substring to find
  start : Optional[int] = the start of the search
  end : Optional[int] = where the search has to end

"""

string : str = "hello world"
print(string.index("world"))
# 6