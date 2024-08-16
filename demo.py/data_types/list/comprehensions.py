"""

[
  statement
  iteration
  condition : Optional
]

"""

num_list : list[int] = [
  number
  for number in range(5)
]
print(num_list)
# [0, 1, 2, 3, 4]


num_list : list[int] = [
  number
  for number in range(10)
  if not number % 2
]
print(num_list)
# [0, 2, 4, 6, 8]