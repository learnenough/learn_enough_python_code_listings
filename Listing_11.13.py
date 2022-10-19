>>> curies = nobel.loc[nobel["surname"].str.contains("Curie", na=False)]
>>> curies
      id firstname  ...   city country
4      5    Pierre  ...  Paris  France
5      6     Marie  ...    NaN     NaN
6      6     Marie  ...  Paris  France
191  194     Irène  ...  Paris  France
