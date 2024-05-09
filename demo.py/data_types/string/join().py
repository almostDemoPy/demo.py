"""

str.join(
  iterable : Iterable
)

- Join elements of the sequence separated by a string separator


Parameters :

iterable : Iterable = objects capable of returning their members
    one at a time. Some examples are :
        List
        Tuple
        String
        Dictionary
        Set

"""

string : str = "sample"
separator : str = "."
print(separator.join(string))
# s.a.m.p.l.e


# Case : list

sample_list : list[str] = ["a", "b", "c"]
separator : str = "."
print(separator.join(sample_list))
# a.b.c


# Case : tuple

sample_tuple : tuple[str] = ("a", "b". "c")
separator : str = "."
print(separator.join(sample_tuple))
# a.b.c


# Case : set

sample_set : set[str] = {"1", "2", "3"}
separator : str = "."
print(separator.join(sample_set))
# 1.2.3


# Case : dictionary

sample_dict : dict[str, int] = {"sample" : 1, "string" : 2}
separator : str = " "
print(separator.join(sample_dict))
# "sample string"