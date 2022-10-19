>>> a = ["ant", "bat", "cat", "42"]
['ant', 'bat', 'cat', '42']
>>> "".join(a)                         # Join on empty space.
'antbatcat42'
>>> ", ".join(a)                       # Join on comma-space.
'ant, bat, cat, 42'
>>> " -- ".join(a)                     # Join on double dashes.
'ant -- bat -- cat -- 42'
