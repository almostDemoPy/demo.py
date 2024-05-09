"""

str.isidentifier()

- Check if a string is a valid identifier


Note : A string gis considered as a valid identifier if :
- it only consists of alphanumeric characters and underscore
- doesn't start with a space or a number

"""

string : str = "abc123"
print(string.isidentifier())
# True


string : str = "abc_123"
print(string.isidentifier())
# True


string : str = "123_abc"
print(string.isidentifier())
# False


string : str = "_abc123"
print(string.isidentifier())
# False