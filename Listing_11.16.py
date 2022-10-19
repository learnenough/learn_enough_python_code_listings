>>> titanic["Age"].notna()
Name
Braund, Mr. Owen Harris                                 True
Cumings, Mrs. John Bradley (Florence Briggs Thayer)     True
Heikkinen, Miss. Laina                                  True
Futrelle, Mrs. Jacques Heath (Lily May Peel)            True
Allen, Mr. William Henry                                True
                                                       ...
Montvila, Rev. Juozas                                   True
Graham, Miss. Margaret Edith                            True
Johnston, Miss. Catherine Helen "Carrie"               False
Behr, Mr. Karl Howell                                   True
Dooley, Mr. Patrick                                     True
Name: Age, Length: 891, dtype: bool
>>> valid_ages = titanic[titanic["Age"].notna()]
