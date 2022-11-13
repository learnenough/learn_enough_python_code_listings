>>> def has_all_digits(numbers):
...     for n in numbers:
...         if set(str(n)) == set("0123456789"):
...             return n
...     return None
