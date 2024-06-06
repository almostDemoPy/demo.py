"""

list[start : stop : step]

===============================================================

Options :

start : int = starting index

stop : int = ending position

step : int = amount of step to take per iteration

"""

# Case : start is provided only

sample_list : list[int] = [1, 2, 3, 4, 5]
print(sample_list[2:])
# [3, 4, 5]


# Case : stop is provided only

sample_list : list[int] = [1, 2, 3, 4, 5]
print(sample_list[:3])
# [1, 2, 3]


# Case : step is provided only

sample_list : list[int] = [1, 2, 3, 4, 5]
print(sample_list[::2])
# [1, 3, 5]


# Case : negative integer is passed in step

sample_list : list[int] = [1, 2, 3, 4, 5]
print(sample_list[::-1])
# [5, 4, 3, 2, 1]


# Case : start and stop is provided

sample_list : list[int] = [1, 2, 3, 4, 5]
print(sample_list[2 : 4])
# [3, 4]


# Case :start, stop, and step is provided

sample_list : list[int] = [1, 2, 3, 4, 5]
print(sample_list[4:2:-1])
# [5, 4]