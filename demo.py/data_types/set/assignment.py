"""

variable_name : set[Union[int, float, str, bool]] = {...}

- Note : sets will be arranged in ascending order

"""

sample_set : set[str] = {"a", "b", "c"}
print(sample_set)
# {"a", "b", "c"}


sample_set : set[int] = {3, 2, 1}
print(sample_set)
# {1, 2, 3}


sample_set : set[float] = {1.0, 0.5, 4.3}
print(sample_set)
# {0.5, 1.0, 4.3}


# Case : booleans are expressed as ints : True = 1 ; False = 0

sample_set : set[bool] = {True, False}
print(sample_set)
# {False, True}


# Case : multiple data types are passed

sample_set : set[Union[int, float, str, bool]] = {123, 23.01, "d", True}
print(sample_set)
# {"d", True, 123, 23.01}