"""

str.zfill(
  length : int
)

- Returns a copy of the string with "0" characters padded to
    the left side of the given string

==============================================================

Parameters :

length : int = the length of the returned string

"""

string : str = "sample string"
print(string.zfill(15))
# "00sample string"


# Case : with sign prefix

string : str = "+sample string"
print(string.zfill(15))
# "+0sample string"

string : str = "--sample string"
print(string.zfill(20))
# "-00000-sample string"