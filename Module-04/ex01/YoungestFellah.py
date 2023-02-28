import pandas as pd
from numpy import NaN
from FileLoader import FileLoader


def youngestFellah(df: pd.DataFrame, year: int) -> dict:
    """The function returns a dictionary containing the age of the youngest woman and man
        who took part in the Olympics on that year. The name of the dictionary's keys is up to
        you, but it must be self-explanatory.
     """
    youngest = {'F': NaN, 'M': NaN}
    if (not (isinstance(df, pd.DataFrame) and isinstance(year, int))):
        return youngest
    df = df[df["Year"] == year].loc[:, ["Sex", "Age"]].sort_values(by=["Age"])
    if len(df) == 0:
        return youngest
    sex_types = df["Sex"].unique()
    dicty = dict()
    for sex in sex_types:
        tmp = df[df["Sex"] == sex]
        v = tmp.iloc[0]
        dicty[v[0]] = v[1]
    keys = list(dicty.keys())
    keys.sort()
    sorted_dict = {i: dicty[i] for i in keys}
    if (len(youngest) == 0):
        return youngest
    return sorted_dict


# if __name__ == "__main__":
#     loader = FileLoader()
#     data = loader.load('../athlete_events.csv')
#     print(youngestFellah(data, 1992))
#     print(youngestFellah(data, 2004))
#     print(youngestFellah(data, 2010))
#     print(youngestFellah(data, 1991))
#     print(youngestFellah(data, 2003))
#     print(youngestFellah(data, "1992"))
