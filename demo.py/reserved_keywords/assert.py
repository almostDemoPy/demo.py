"""

assert

- Usually used for debugging

"""

def divide(
  x : int | float,
  y : int | float
) -> int | float:
  assert y != 0, "Cannot be divided by 0"
  return x / y

print(divide(1, 0))
# "Cannot be divided by 0"