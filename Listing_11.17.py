titanic[(titanic["Sex"] == "female") &
        (titanic["Pclass"] == 3)]["Survived"].mean()
