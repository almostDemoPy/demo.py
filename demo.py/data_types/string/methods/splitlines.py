"""

str.splitlines(
  keepends : Optional[Union[int, bool]]
)

- Split the lines at line boundaries

================================================================

Parameters :

keepends : Optional[Union[int, bool]] = When set to TRUE, line
    breaks are included in the resulting list. This can be a
    number specifying the position of line break

================================================================

splitlines() splits on the following line boundaries :

\n - Line Feed

\r - Carriage Return

\x1c - File Separator

\x1d - Group Separator

\x1e - Record Separator

\x85 - Next Line

\v or \x0b - Line Tabulation

\f or \x0c - Form Feed

\u2028 - Line Separator

\u2029 - Paragraph Separator

"""

string : str = "sample\nstring"
print(string.splitlines())
# ["sample", "string"]


# Case : boolean is passed

print(string.splitlines(True))
# ["sample\n", "string"]


# Case : integers are passed

print(string.splitlines(0))
# ["sample", "string"]

print(string.splitlines(1))
# ["sample\n", "string"]