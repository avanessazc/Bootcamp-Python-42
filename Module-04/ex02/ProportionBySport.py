import pandas as pd
from numpy import NaN
from FileLoader import FileLoader


def proportion_by_sport(df: pd.DataFrame, year: int, sport: str, gender: str) -> float or None:
    """The function returns a float corresponding to the proportion (percentage) of
        participants who played the given sport among the participants of the given gender.
        The function answers questions like the following : "What was the percentage of
        female basketball players among all the female participants of the 2016 Olympics?"
    """
    if (not (isinstance(df, pd.DataFrame) and isinstance(year, int) and
            isinstance(sport, str) and gender in ['F', 'M'])):
        return None
    df = df[(df["Year"] == year) & (df["Sex"] == gender)]
    df = df.drop_duplicates(subset=["ID"])
    df_res = df[df["Sport"] == sport]
    return (df_res.shape[0] / df.shape[0])


# if __name__ == "__main__":
#     loader = FileLoader()
#     data = loader.load('../athlete_events.csv')
#     print(proportion_by_sport(data, 2004, 'Tennis', 'F'))
#     print(proportion_by_sport(data, 2008, 'Hockey', 'F'))
#     print(proportion_by_sport(data, 1964, 'Biathlon', 'M'))
#     print(proportion_by_sport(data, 1964, 'Biathlon', 'G'))
