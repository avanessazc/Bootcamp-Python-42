import pandas as pd
from sys import stderr


class FileLoader:

    def load(self, path: str) -> pd.DataFrame or None:
        """takes as an argument the file path of the dataset to load,
            displays a message specifying the dimensions of the dataset (e.g. 340 x 500) and
            returns the dataset loaded as a pandas.DataFrame.
        """
        df = None
        try:
            df = pd.read_csv(path)
            print(f"Loading dataset of dimensions {df.shape[0]} x {df.shape[1]}")
        except Exception as e:
            print(f"Exception: {e.__class__.__name__}: {e.strerror if hasattr(e, 'strerror') else e}", file=stderr)
        return df

    def display(self, df: pd.DataFrame, n: int) -> None:
        """takes a pandas.DataFrame and an integer as arguments,
            displays the first n rows of the dataset if n is positive, or the last n rows if n is
            negative.
        """
        if (not (isinstance(df, pd.DataFrame) and isinstance(n, int))):
            print("It is not possible to display pandas.DataFrame", file=stderr)
            return
        res = df[:n] if (n >= 0) else df[n:]
        print(res)


# if __name__ == "__main__":
#     loader = FileLoader()

#     data = loader.load("./athlete_events.csv")
#     loader.display(data, 3)
#     print("\n")
#     data = loader.load(4)
#     loader.display(data, 0)
#     print("\n")
#     data = loader.load("../athlete_events.csv")
#     loader.display(data, 3)
