import numpy as np

class ScrapBooker:

    @staticmethod
    def __check_array(array: np.ndarray) -> bool:
        if (not (isinstance(array, np.ndarray))):
            return False
        return True

    @staticmethod
    def __check_shape(shape: tuple) -> bool:
        if (not (isinstance(shape, tuple) and len(shape) == 2 and
                all([(isinstance(obj, int) and obj >= 0) for obj in shape]))):
            return False
        return True

    def crop(self, array: np.ndarray, dim: tuple, position: tuple =(0,0)) -> np.ndarray or None:
        """
        Crops the image as a rectangle via dim arguments (being the new height
        and width of the image) from the coordinates given by position arguments.
        Args:
        -----
        array: numpy.ndarray
        dim: tuple of 2 integers.
        position: tuple of 2 integers.
        Return:
        -------
        new_arr: the cropped numpy.ndarray.
        None (if combinaison of parameters not compatible).
        Raise:
        ------
        This function should not raise any Exception.
        """
        if (not (self.__check_array(array) and
                self.__check_shape(dim) and
                self.__check_shape(position))):
            return None
        # check if position is inside
        if (array.shape[0] < position[0] or array.shape[1] < position[1]):
            return None
        # find max size of the new array
        max_size = (array.shape[0] - position[0], array.shape[1] - position[1])
        # check if dim < max size
        if (max_size[0] < dim[0] or max_size[1] < dim[1]):
            return None
        # create new array
        cropped = array[position[0]:(position[0] + dim[0]), position[1]:(position[1] + dim[1])]
        return cropped
    
    def thin(self, array: np.ndarray, n: int, axis: int) -> np.ndarray or None:
        """
        Deletes every n-th line pixels along the specified axis (0: Horizontal, 1: Vertical)
        Args:
        -----
        array: numpy.ndarray.
        n: non null positive integer lower than the number of row/column of the array
        (depending of axis value).
        axis: positive non null integer.
        Return:
        -------
        new_arr: thined numpy.ndarray.
        None (if combinaison of parameters not compatible).
        Raise:
        ------
        This function should not raise any Exception.
        """
        if (not (self.__check_array(array) and
                isinstance(n, int) and n > 0 and
                isinstance(axis, int) and (axis == 0 or axis == 1))):
            return None
        axis = int(not axis)
        to_delete = list(range(n - 1, array.shape[axis], n))
        new_arr = np.delete(array, to_delete, axis=axis)
        return new_arr

    def juxtapose(self, array: np.ndarray, n: int, axis: int) -> np.ndarray or None:
        """
        Juxtaposes n copies of the image along the specified axis.
        Args:
        -----
        array: numpy.ndarray.
        n: positive non null integer.
        axis: integer of value 0 or 1.
        Return:
        -------
        new_arr: juxtaposed numpy.ndarray.
        None (combinaison of parameters not compatible).
        Raises:
        -------
        This function should not raise any Exception.
        """
        if (not (self.__check_array(array) and
                isinstance(n, int) and n > 0 and
                isinstance(axis, int) and (axis == 0 or axis == 1))):
            return None

        new_arr = np.copy(array)
        for i in range(n - 1):
            new_arr = np.concatenate((new_arr, array), axis=axis)
        return new_arr

    def mosaic(self, array: np.ndarray, dim: tuple) -> np.ndarray or None:
        """
        Makes a grid with multiple copies of the array. The dim argument specifies
        the number of repetition along each dimensions.
        Args:
        -----
        array: numpy.ndarray.
        dim: tuple of 2 integers.
        Return:
        -------
        new_arr: mosaic numpy.ndarray.
        None (combinaison of parameters not compatible).
        Raises:
        -------
        This function should not raise any Exception.
        """
        tmp = self.juxtapose(array, dim[0], 0)
        new_arr = self.juxtapose(tmp, dim[1], 1)
        return new_arr

if __name__ == "__main__":
    spb = ScrapBooker()
    arr1 = np.arange(0,25).reshape(5,5)
    print(arr1)
    print("\n")
    print(spb.crop(arr1, (4,5),(1,0)))
    print("\n")
    arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1,9)
    print(arr2)
    print("\n")
    print(spb.thin(arr2,3,0))
    print("\n")
    arr3 = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])
    print(spb.juxtapose(arr3, 3, 1))
    print("\n")
    arr4 = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])
    print(spb.mosaic(arr4, (3, 3)))
