import pandas as pd
from numpy import NaN
from FileLoader import FileLoader


class SpatioTemporalData:

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def when(self, location: str) -> list or None:
        """
        takes a location as an argument and returns a list containing the
        years where games were held in the given location
        """
        if (not (isinstance(self.df, pd.DataFrame) and
                isinstance(location, str))):
            return None
        df = self.df[self.df["City"] == location]
        listy = df["Year"].drop_duplicates().to_list()
        return (listy)

    def where(self, date: int) -> str or None:
        """
        takes a date as an argument and returns the location where the
        Olympics took place in the given year
        """
        if (not (isinstance(self.df, pd.DataFrame) and isinstance(date, int))):
            return None
        df = self.df[self.df["Year"] == date]
        listy = df["City"].drop_duplicates().to_list()
        return (listy)


# if __name__ == "__main__":
#     loader = FileLoader()
#     data = loader.load('../athlete_events.csv')
#     sp = SpatioTemporalData(data)

#     print(sp.where(1896))
#     print(sp.where(2016))
#     print(sp.when('Athina'))
#     print(sp.when('Paris'))
