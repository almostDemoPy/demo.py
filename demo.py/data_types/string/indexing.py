"""

Indexing in Python is simple :

str[int]

where int is the index of the character
you are trying to access. Indeces starts
with 0, unlike positions that start with
1.

So per say, str[0] will retrieve the
first character, that is if the length
of the string is at least 1. Otherwise
it will return an error.

Inputting negative integers, starting
from -1, will start accessing the
characters from right-most to the
left-most.

"""

string : str = "sample string"
print(string[0])
# "s"


string : str = "hello world"
print(string[0])
# "h"


# Case : negative integer

string : str = "sample string"
print(string[-1])
# "g"