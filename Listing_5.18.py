>>> def squares_generator():
...     for n in range(10**8 + 1):
...         yield n**2
...
>>> squares = squares_generator()
