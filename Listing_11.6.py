>>> a[np.isclose(a, 0)]
array([ 6.1232340e-17, -1.8369702e-16])
>>> a[np.isclose(a, 0)] = 0
>>> a
array([ 1.,  0., -1.,  0.,  1.])
