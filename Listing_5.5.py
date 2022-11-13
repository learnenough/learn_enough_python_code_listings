>>> def deriver(f, x):
...     h = 0.00001
...     return (f(x+h) - f(x))/h
...
>>> deriver(square, 3)
6.000009999951316
