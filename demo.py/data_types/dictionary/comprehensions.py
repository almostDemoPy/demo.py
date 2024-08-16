"""

{
  key : value
  iteration
  condition : Optional
}

"""


squares : dict[int, int] = {
  number : number ** 2
  for number in range(5)
}
print(squares)
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


numbers : dict[int, int] = {
  number : number % 2
  for number in range(5)
  if number % 2
}
print(numbers)
# {1: 1, 3: 1}