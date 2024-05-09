"""

str.isprintable()

- Check if all characters in a string are printable or the string is empty

Printable characters are :
  - Digits : 0123456789
  - Uppercase letters : ABCDEFGHIJKLMNOPQRSTUVWXYZ
  - Lowercase letters : abcdefghijklmnopqrstuvwxyz
  - Punctuation characters : !”#$%&'()*+, -./:;?@[\]^_`{ | }~
  - Space

"""

string : str = "hello world"
print(string.isprintable())
# True


string : str = "hello \n world"
print(string.isprintable())
# False


# Case : empty string

string : str = ""
print(string.isprintable())
# True