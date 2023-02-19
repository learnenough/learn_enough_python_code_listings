>>> from math import tau
>>> from numpy.random import default_rng
>>> rng = default_rng()
>>> df = pd.DataFrame(
...     {
...         "Number": 1.0,
...         "String": "foo",
...         "Angles": np.linspace(0, tau, 5),
...         "Random": pd.Series(rng.standard_normal(5)),
...         "Timestamp": pd.Timestamp("20221020"),
...         "Size": pd.Categorical(["tiny", "small", "mid", "big", "huge"])
...     })
>>> df
   Number String    Angles    Random  Timestamp    Size
0     1.0    foo  0.000000 -1.954002 2022-10-20    tiny
1     1.0    foo  1.570796  0.967171 2022-10-20   small
2     1.0    foo  3.141593 -1.149739 2022-10-20     mid
3     1.0    foo  4.712389 -0.084962 2022-10-20     big
4     1.0    foo  6.283185  0.310634 2022-10-20    huge
