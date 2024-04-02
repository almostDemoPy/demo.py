"""

str.endswith(
  suffix : str,
  start : Optional[int],
  end : Optional[int]
)

- Returns a boolean if the string ends with the given suffix


Parameters :

suffix : str = a string to be checked as suffix

start : Optional[int] = starting index

end : Optional[int] = ending index

"""

string : str = "sample"
print(string.endswith("ple"))

# Output :
# True


string : str = "sample"
print(string.endswith("pl"))

# Output :
# False