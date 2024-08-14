"""

finally

- Always executes after the try-except block
    regardless of the error, if any

"""

try:
  raise Exception("an error occured")
except Exception:
  print("fix the errors")
  # "fix the errors"
finally:
  print("complete the code")
  # "complete the code"