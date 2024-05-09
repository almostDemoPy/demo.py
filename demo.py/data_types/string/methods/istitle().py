"""

str.istitle()

- Check if all the words in the string are title-cased

Note :
  - A string is title-cased when all words begin with uppercase
      letters and the remaining characters are lowercase letters

"""

string : str = "Sample String"
print(string.istitle())
# True


string : str = "Sample string"
print(string.istitle())
# False


# Case : one or more word contains uppercase characters
#     in the middle

string : str = "SAMPLE String"
print(string.istitle())
# False


# Case : contains digits

string : str = "123 String"
print(string.istitle())
# True