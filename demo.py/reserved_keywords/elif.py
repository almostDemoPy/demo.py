"""

elif

- Shorthand for else if, checks if some other
    condition holds when the previous
    if statement or elif statement is False

"""


number : int | float = 5
if number < 5:
  print(-1)
elif number == 5:
  print(0)
  # 0
else:
  print(1)