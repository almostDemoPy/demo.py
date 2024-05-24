"""

str.rfind(
  substring : str,
  start : Optional[int] = 0,
  end : Optional[int] = length - 1
)

- Return the rightmost index of the substring if found in the
    given string. If not found then it returns -1

===============================================================

Parameters :

substring : str = substring to look for

start : Optional[int] = starting position of the search

end : Optional[int] = Ending position of the search

"""

string : str = "sample string"
print(string.rfind("string"))
# 7


# Case : substring is not found

string : str = "sample string"
print(string.rfind("python"))
# -1