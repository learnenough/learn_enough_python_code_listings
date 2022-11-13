male_passengers = titanic[titanic["Sex"] == "male"]
female_passengers = titanic[titanic["Sex"] == "female"]
valid_male_ages = male_passengers[titanic["Age"].notna()]
valid_female_ages = female_passengers[titanic["Age"].notna()]
