import pandas as pd
import matplotlib.pyplot as plt
from FileLoader import FileLoader

class Komparator:

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def compare_box_plots(self, categorical_var: str, numerical_var: str) -> None:
        """
        displays a series of box plots to compare how the distribution of the numerical variable changes
        if we only consider the subpopulation which belongs to each category. There should
        be as many box plots as categories. For example, with Sex and Height, we would
        compare the height distributions of men vs. women with two box plots.
        """
        df = self.df[[categorical_var, numerical_var]].dropna()
        features = df[categorical_var].unique()

        fig, ax = plt.subplots(ncols=len(features))
        for i, feat in enumerate(features):
            ax[i].set_title(feat)
            ax[i].boxplot(df[df[categorical_var] == feat][numerical_var])
        plt.show()

    def density(self, categorical_var: str, numerical_var: str) -> None:
        """
        displays the density of the
        numerical variable. Each subpopulation should be represented by a separate curve
        on the graph.
        """
        df = self.df[[categorical_var, numerical_var]].dropna()
        features = df[categorical_var].unique()

        fig, ax = plt.subplots(nrows=len(features))
        for i, feat in enumerate(features):
            ax[i].set_title(feat)
            df[df[categorical_var] == feat][numerical_var].plot(kind='density', ax=ax[i], label=numerical_var)
            ax[i].legend()
        fig.tight_layout()
        plt.show()

    def compare_histograms(self, categorical_var: str, numerical_var: str) -> None:
        """
        plots the numerical variable in a separate histogram for each category. As an extra, you can
        use overlapping histograms with a color code.
        """
        df = self.df[[categorical_var, numerical_var]].dropna()
        features = df[categorical_var].unique()

        fig, ax = plt.subplots(nrows=len(features))
        for i, feat in enumerate(features):
            ax[i].set_title(feat)
            ax[i].hist(df[df[categorical_var] == feat][numerical_var], label=numerical_var)
            ax[i].legend()
        plt.show()


if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('../athlete_events.csv')
    k = Komparator(data)

    k.compare_histograms("Sex", "Age")
    k.density("Medal", "Age")
    k.compare_box_plots("Medal", "Age")
    k.compare_histograms("Medal", "Age")
