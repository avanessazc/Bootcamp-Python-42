import numpy as np
import csv
import sys
import re
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D


class CsvReader():
    def __init__(self,
                 filename=None,
                 sep=',',
                 header=False,
                 skip_top=0,
                 skip_bottom=0):
        if (not (isinstance(filename, str) and
                 isinstance(sep, str) and
                 isinstance(header, bool) and
                 isinstance(skip_top, int) and
                 isinstance(skip_bottom, int))):
            exit("Wrong arguments")
        self.filename = filename
        self.sep = sep
        self.has_header = header
        self.skip_top = skip_top + header
        self.skip_bottom = skip_bottom
        self.fd = None
        self.data = []
        self.header = None

    def __enter__(self):
        try:
            self.fd = open(self.filename, 'r')
            csv_reader = csv.reader(self.fd, delimiter=self.sep)
        except Exception:
            return (None)

        expected_len = None
        for i, row in enumerate(csv_reader):
            if (expected_len is None):
                expected_len = len(row)
            elif (expected_len != len(row)):
                return None

            # check if there is empty line
            for element in row:
                if (len(element) == 0):
                    return None

            if (i == 0 and self.has_header is True):  # set the header
                self.header = row
            elif (i >= self.skip_top and
                    (self.skip_bottom == 0 or i < self.skip_bottom)):
                self.data.append(row)
        return (self)

    def __exit__(self, exception_type, exception_value, exception_traceback):
        if (hasattr(self, 'fd') and self.fd is not None):
            self.fd.close()

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Return:
        nested list (list(list, list, ...)) representing the data.
        """
        return (self.data)

    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """
        return (self.header)

# https://towardsdatascience.com/kmeans-hyper-parameters-explained-with-examples-c93505820cd3
class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid  # number of centroids
        self.max_iter = max_iter  # number of max iterations to update the centroids
        self.centroids = []  # values of the centroids

    def fit(self, X: np.ndarray) -> None:
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        Args:
        -----
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
        None.
        Raises:
        -------
        This function should not raise any Exception.
        """
        self.kmeans = KMeans(init='random',
                             n_clusters=self.ncentroid,
                             n_init=self.max_iter)
        self.kmeans.fit(X)

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predict from wich cluster each datapoint belongs to.
        Args:
        -----
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
        the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
        -------
        This function should not raise any Exception.
        """
        self.cluster_labels = self.kmeans.predict(X)
        self.centroids = self.kmeans.cluster_centers_
        return self.centroids

    def clusters(self, X: np.ndarray) -> None:
        cluster_labels = self.cluster_labels
        cluster_centers = self.centroids
        for i in range(self.ncentroid):
            mask = cluster_labels == i
            center = cluster_centers[i]
            print(f'{sum(mask)} individuals for centroid {i}: \
Height: {center[0]:.5}, Weight: {center[1]:.5}, Bone Density: {center[2]:.5}')


def get_info() -> list or None:
    if (len(sys.argv) != 4):
        return None
    regex_args = [
        rf"^filepath=(.+\.csv)$",
        rf"^ncentroid=(\d+)$",
        rf"^max_iter=(\d+)$",
    ]  # https://realpython.com/python-formatted-output/
    args = []
    for i, regex in enumerate(regex_args):
        search_arg = re.search(regex_args[i], sys.argv[i + 1])
        if (search_arg is None):
            return None
        args.append(search_arg.group(1))
    return args


def main():
    # parsing the arguments
    args = get_info()
    if (args is None):
        print("Wrong arguments")
    if (args is not None):
        data = []
        # reading the dataset
        with CsvReader(args[0], header=True, skip_top=1) as file:
            if (file is None):
                print("File is corrupted\n")
                try:
                    print("Fixing file...\n")
                    data = np.genfromtxt(args[0], delimiter=",", skip_header=1)
                except Exception as e:
                    print(e)
                    return
            else:
                data = np.array(file.getdata())
        X = data[:, 1:]  # Delete index
        ncentroid = int(args[1])
        max_iter = int(args[2])

        k = KmeansClustering(max_iter=max_iter, ncentroid=ncentroid)
        # fit the dataset
        k.fit(X)
        # display the coordinates of the different centroids
        print("Coordinates of the centroids:")
        print(k.predict(X))
        print("\n")
        # display the number of individuals associated to each centroid
        k.clusters(X)


if __name__ == "__main__":
    main()
