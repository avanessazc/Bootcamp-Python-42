import pandas as pd
from numpy import NaN
from FileLoader import FileLoader

def how_many_medals(df: pd.DataFrame, name: str) -> dict or None:
    """The function returns a dictionary of dictionaries giving the number and type of medals
        for each year during which the participant won medals. The keys of the main dictionary are the
        Olympic games years. In each year's dictionary, the keys are 'G', 'S', 'B'
        corresponding to the type of medals won (gold, silver, bronze). The innermost values
        correspond to the number of medals of a given type won` for a given year,
    """
    if (not (isinstance(df, pd.DataFrame) and isinstance(name, str))):
        return None
    dicty = dict()
    data = df[(df["Name"] == name)]
    years = data["Year"].unique()
    for yr in years:
        medals = [0, 0, 0]
        tmp = data[(data["Year"] == yr) & (data["Medal"] == "Gold")]
        medals[0] = tmp["Medal"].count()
        tmp = data[(data["Year"] == yr) & (data["Medal"] == "Silver")]
        medals[1] = tmp["Medal"].count()
        tmp = data[(data["Year"] == yr) & (data["Medal"] == "Bronze")]
        medals[2] = tmp["Medal"].count()
        sub_dicty = dict()
        sub_dicty["G"] = medals[0]
        sub_dicty["S"] = medals[1]
        sub_dicty["B"] = medals[2]
        dicty[yr] = sub_dicty
    return (dicty)


# if __name__ == "__main__":
#     loader = FileLoader()
#     data = loader.load('../athlete_events.csv')
#     print(how_many_medals(data, "Kjetil Andr Aamodt"))
#     print(how_many_medals(data, "Yekaterina Konstantinovna Abramova"))
#     print(how_many_medals(data, "Kristin Otto"))
#     print(how_many_medals(data, "None"))
