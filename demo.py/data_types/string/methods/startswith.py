"""

str.startswith(
  prefix : str,
  start : Optional[int],
  end : Optional[int]
)

- Check if a string starts with the specified prefix

===============================================================

Parameters :

prefix : str = a substring

start : Optional[int] = starting position of the search

end : Optional[int] = ending position of the search

"""

string : str = "sample string"
print(string.startswith("sample"))
# True

print(string.startswith("string"))
# False

print(string.startswith("string", 7))
# True


# Case : check if multiple strings

print(string.startswith(("python", "string", "sample", "demo")))
# True