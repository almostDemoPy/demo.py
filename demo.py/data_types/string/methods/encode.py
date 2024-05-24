"""

str.encode(
  encoding : str,
  errors : Optional[str] = Literal[
    "strict", "ignore", "replace",
    "xmlcharrefreplace", "backslashreplace", "namereplace"
  ]
)

- Convert the string into a collection of bytes

===============================================================

Parameters :

encoding : str = the encoding on the basis of which encoding
    has to be performed

errors : Optional[str] = decides how to handle the error if
    they occur. There are six types of error response :
        strict - default response which raises a
            UnicodeDecodeError exception on failure
        ignore - ignores the unencodable unicode from the
            result
        replace - replaces the unencodable unicode to a
            question mark
        xmlcharrefreplace - inserts XML character reference
            instead of unencodable unicode
        backslashreplace - isnerst a \uNNNN escape sequence
            instead of unencodable unicode
        namereplace - inserts \N{...} escape sequence instead
            of unencodable unicode

"""

string : str = "¶"
print(string.encode("utf-8"))
# b'\xc2\xb6'


string : str = "123-¶"
print(string.encode("ascii", errors = "ignore"))
# b'123-'