>>> def foo(*args, **kwargs):
...     print(args)
...     print(kwargs)
...
>>> foo("This", "is a bunch", "of arguments", "to the function",
...     a="hello", b="world", bar="good day!")
