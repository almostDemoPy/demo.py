"""

str.center(
  length : int,
  fillchar : str
)

- returns a new padded string with the specified character


Parameters:

length : int = length of the string after padding

fillchar : Optional[str] = character which need to be padded. If not provided, defaults to space

"""

string : str = "sample"
print(string.center(10, "#"))

# Output :
# ##sample##


# Case : LENGTH is less than the length of the string

string : str = "sample"
print(string.center(5, "#"))

# Output :
# sample


# Case : FILLCHAR is at least 2 characters long

string : str = "sample"
print(string.center(20, "ab"))

# Output :
# TypeError: The fill character must be exactly one character long