"""

str.rsplit(
  separator : str,
  max_split : Optional[int]
)

- Return a list of strings after breaking the given string from
    the right side by the specified separator

===============================================================

Parameters :

separator : str = the substring to split the string

max_split : Optional[int] = maximum splits to process. Defaults
    to no limits

"""

string : str = "sample python string"
print(string.rsplit(" "))
# ["sample", "python", "string"]


string : str = "sample python string"
print(string.rsplit(" ", 1))
# ["sample python", "string"]


# Case : separator is not found

string : str = "sample string"
print(string.rsplit("python"))
# ["sample string"]