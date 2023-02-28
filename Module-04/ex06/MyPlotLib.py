import pandas as pd
import matplotlib.pyplot as plt
from FileLoader import FileLoader


class MyPlotLib:

    @staticmethod
    def __check_args(df: pd.DataFrame, features: list) -> None:
        if (not isinstance(df, pd.DataFrame)):
            return False
        columns = df.columns.values
        if (not (isinstance(features, list) and
            all([(isinstance(obj, str) and (obj in columns) and
                df[obj].dtype.kind in 'iuf') for obj in features]) and
                len(features) > 0)):
            # https://numpy.org/doc/stable/reference/generated/numpy.dtype.kind.html
            return False
        return True

    def histogram(self, df: pd.DataFrame, features: list) -> None:
        """
        plots one histogram for each numerical feature in the list
        """
        if (self.__check_args(df, features) is True):
            df[features].hist()
            plt.show()

    def density(self, df: pd.DataFrame, features: list) -> None:
        """
        plots the density curve of each numerical feature in the list
        """
        if (self.__check_args(df, features) is True):
            pd.DataFrame(df[features]).plot(kind='density')
            plt.show()

    def pair_plot(self, df: pd.DataFrame, features: list) -> None:
        """
        plots a matrix of subplots (also called scatter plot
        matrix). On each subplot shows a scatter plot of one numerical variable against
        another one. The main diagonal of this matrix shows simple histograms.
        """
        if (self.__check_args(df, features) is True):
            pd.plotting.scatter_matrix(df[features])
            plt.show()

    def box_plot(self, df: pd.DataFrame, features: list) -> None:
        """
        displays a box plot for each numerical variable in the dataset.
        """
        if (self.__check_args(df, features) is True):
            fig, ax = plt.subplots()
            ax.boxplot(df[features].dropna(), labels=features)
            plt.show()


# if __name__ == "__main__":
#     loader = FileLoader()
#     data = loader.load('../athlete_events.csv')
#     mpl = MyPlotLib()
#     mpl.histogram(data, ["Weight", "Height"])
#     mpl.density(data, ["Weight", "Height"])
#     mpl.pair_plot(data, ["Weight", "Height"])
#     mpl.box_plot(data, ["Weight", "Height"])
