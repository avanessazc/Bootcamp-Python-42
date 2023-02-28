import pandas as pd
from numpy import NaN
from FileLoader import FileLoader


def how_many_medals_by_country(df: pd.DataFrame, country_name: str) -> dict or None:
    """
        The function returns a dictionary of dictionaries giving the number and type of medal
        for each competition where the country delegation earned medals. The keys of the main
        dictionary are the Olympic games' years. In each year's dictionary, the key are 'G', 'S',
        'B' corresponding to the type of medals won.
    """
    team_sports = ['Basketball', 'Football', 'Tug-Of-War', 'Badminton', 'Sailing', 'Handball', 'Water Polo', 'Hockey', 'Rowing', 'Bobsleigh', 'Softball', 'Volleyball', 'Synchronized Swimming', 'Baseball', 'Rugby Sevens', 'Rugby', 'Lacrosse', 'Polo']
    if (not (isinstance(df, pd.DataFrame) and isinstance(country_name, str))):
        return None

    df = df[df["Team"] == country_name]
    df = df.loc[:, ['Team', 'Games', 'Year', 'Sport', 'Event', 'Medal']]
    df_teams = df[df['Sport'].isin(team_sports)].drop_duplicates()
    df_solo = df[~df['Sport'].isin(team_sports)]
    df = pd.concat([df_teams, df_solo]).loc[:, ['Year', 'Medal']]

    data = df.groupby(['Year'])['Medal'].apply(list).to_dict()
    for year in data.keys():
        data[year] = {
            'G': data[year].count('Gold'),
            'S': data[year].count('Silver'),
            'B': data[year].count('Bronze')
        }
    return (data)


if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('../athlete_events.csv')
    print(how_many_medals_by_country(data, "United States"))
