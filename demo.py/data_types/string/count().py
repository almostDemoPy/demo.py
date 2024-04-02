"""

str.count(
  substring : str,
  start : Optional[int],
  end : Optional[int]
)

- Returns the number of occurences of a substring within a string


Parameters :

substring : str = substring whose count is to be found

start : Optional[int] = starting index

end : Optional[int] = ending index

"""

string : str = "sample"
print(string.count("a"))

# Output :
# 1


string : str = "HelLo World"
print(string.count("l"))

# Output :
# 2


string : str = "hello world"
print(string.count("l", 0, 4))

# Output :
# 2