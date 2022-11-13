>>> def has_all_digits(numbers):
...     for n in numbers:
...         if set(str(n)) == set("0123456789"):
...             return n
...     return None
...
>>> has_all_digits([1424872341, 1236490835741, 12341960523])
1236490835741
