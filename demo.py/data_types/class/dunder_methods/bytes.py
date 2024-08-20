"""

class Class:
  def __bytes__(self) -> bytes:
    ...

- Implements the built-in bytes() function

"""

class Sample:
  def __bytes__(self) -> bytes:
    return bytes(42)


sample : Sample = Sample()
print(bytes(sample))
# b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00
# \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
# x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
# x00\x00\x00\x00\x00\x00'