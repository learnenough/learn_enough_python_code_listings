>>> soliloquy = "To be, or not to be, that is the question:"
>>> a = ["badger", 42, "To be" in soliloquy]
>>> a
['badger', 42, True]
>>> a[2]
True
>>> a[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
