"""

dictionary.get(
  key : Union[int, float, str, bool],
  value : Optional[Any] = None
)

- Returns the value for the given key if present in the
    dictionary

===============================================================

Parameters :

key : Union[int, float, str, bool] = the key name of the item
    you want to return the value from

value : Optional[Any] = value to be returned if the key is not
    found. Defaults to None

"""

dictionary : dict[int, int] = {
  1 : 2,
  3 : 4,
  5 : 6
}
print(dictionary.get(3))
# 4


# Case : key name does not exist

dictionary : dict[int, int] = {
  1 : 2,
  3 : 4,
  5 : 6
}
print(dictionary.get(7))
# None


# Case : key name does not exist and value is provided

dictionary : dict[int, int] = {
  1 : 2,
  3 : 4,
  5 : 6
}
print(dictionary.get(7, "Does Not Exist"))
# "Does Not Exist"