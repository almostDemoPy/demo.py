"""

raise

- Used to raise an exception / error

"""

age : str = "seventeen"
if not isinstance(age, int):
  raise TypeError("Age must be an integer")
  # TypeError: Age must be an integer