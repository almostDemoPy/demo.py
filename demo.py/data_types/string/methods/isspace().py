"""

str.isspace()

- Check if all characters in the string are whitespace characters

Whitespace characters are :
  - Space
  - Horizontal tab : \t
  - Newline : \n
  - Vertical tab : \v
  - Feed : \f
  - Carriage return : \r

"""

string : str = "\n\n"
print(string.isspace())
# True


string : str = "hello\tworld"
print(string.isspace())
# False