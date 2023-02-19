>>> laureates = nobel.groupby(["id", "firstname", "surname"])
>>> sizes = laureates.size()
>>> sizes[sizes > 1]
id   firstname  surname
6    Marie      Curie      2
66   John       Bardeen    2
217  Linus      Pauling    2
222  Frederick  Sanger     2
