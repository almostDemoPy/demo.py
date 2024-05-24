"""

str.rindex(
  substring : str,
  start : Optional[int] = 0,
  end : Optional[int] = length - 1
)

- Return the highest index of the subsbtring inside the string

===============================================================

Parameters :

substring : str = substring to search for

start : Optional[int] = starting position of the search

end : Optional[int] = ending position of the search

===============================================================

Exceptions :

ValueError : substring is not found

"""

string : str = "sample string"
print(string.rindex("string"))
# 7


# Case : substring is not Found

string : str = "sample string"
print(string.rindex("python"))
# ValueError: substring is not found