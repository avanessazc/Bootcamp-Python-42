import numpy as np
from copy import deepcopy
from ImageProcessor import ImageProcessor

# https://www.degeneratestate.org/posts/2016/Oct/23/image-processing-with-numpy/
# https://towardsdatascience.com/image-processing-with-python-color-isolation-for-beginners-3b472293335b


class ColorFilter:

    @staticmethod
    def __check_ndarray(array: np.ndarray) -> bool:
        if (not (isinstance(array, np.ndarray) and
                ('float' in str(array.dtype) or 'int' in str(array.dtype)))):
            return False
        return True

    @staticmethod
    def __check_grayscale_args(filter: str, **kwargs) -> bool:
        # print("len(kwargs): ", len(kwargs))
        weights = kwargs.pop('weights', None)
        # weights = kwargs.get('weights', None)
        # print("weights: ", weights)
        # hasWeights = weights is not None

        if (
            (len(kwargs) != 0) or
            (filter not in ['m', 'mean', 'w', 'weight']) or
            (filter in ['m', 'mean'] and (weights is not None)) or
            (filter in ['w', 'weight'] and (
                not isinstance(weights, list) or
                len(weights) != 3 or
                not all([isinstance(obj, float) and
                    obj >= 0 for obj in weights]) or
                np.sum(weights) != 1.
                ))
          ):
            return False
        return True

    def invert(self, array: np.ndarray) -> np.ndarray:
        """
        Inverts the color of the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if (not self.__check_ndarray(array)):
            return None
        # https://yashaslokesh.github.io/inverting-the-colors-of-an-image.html
        # Mathematically, to invert the color of one pixel, we subtract the pixel's color
        # values from the maximum, 255. If we have a PNG format image, then we have an extra
        # alpha channel that we don't want to modify, or the transparent parts of the image won't
        # be transparent anymore.
        new_array = 1 - array
        new_array[Ellipsis, 3:] = array[Ellipsis, 3:]  # numpy slice notation re-assign the original extra alpha channel.
        return new_array

    def to_blue(self, array: np.ndarray) -> np.ndarray:
        """
        Applies a blue filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if (not self.__check_ndarray(array)):
            return None
        new_array = np.zeros(array.shape)
        new_array[Ellipsis, 2:] = array[Ellipsis, 2:]
        return new_array

    def to_green(self, array: np.ndarray) -> np.ndarray:
        """
        Applies a green filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if (not self.__check_ndarray(array)):
            return None
        new_array = array.copy()
        new_array[Ellipsis, :3:2] = new_array[Ellipsis, :3:2] * 0
        return new_array

    def to_red(self, array: np.ndarray) -> np.ndarray:
        """
        Applies a red filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if (not self.__check_ndarray(array)):
            return None
        set_blue_green = ColorFilter.to_blue(self, array) + ColorFilter.to_green(self, array)
        new_array = array - set_blue_green
        new_array[Ellipsis, 3:] = array[Ellipsis, 3:]
        return new_array

    def to_celluloid(self, array: np.ndarray) -> np.ndarray:
        """
        Applies a celluloid filter to the image received as a numpy array.
        Celluloid filter must display at least four thresholds of shades.
        Be careful! You are not asked to apply black contour on the object,
        you only have to work on the shades of your images.
        Remarks:
        celluloid filter is also known as cel-shading or toon-shading.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if (not self.__check_ndarray(array)):
            return None
        new_array = array.copy()
        thresholds = np.linspace(array.min(), array.max(), num=4, endpoint=False)
        for shade in thresholds:
            new_array[array >= shade] = shade
        new_array[Ellipsis, 3:] = array[Ellipsis, 3:]
        return new_array

    def to_grayscale(self, array: np.ndarray, filter, **kwargs):
        """
        Applies a grayscale filter to the image received as a numpy array.
        For filter = 'mean'/'m': performs the mean of RBG channels.
        For filter = 'weight'/'w': performs a weighted mean of RBG channels.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        filter: string with accepted values in ['m','mean','w','weight']
        weights: [kwargs] list of 3 floats where the sum equals to 1,
        corresponding to the weights of each RBG channels.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if (not self.__check_ndarray(array)):
            return None
        if (self.__check_grayscale_args(filter, **kwargs) is False):
            return None
        if (filter in ['m', 'mean']):
            for row in array:
                for pixel in row:
                    gray = pixel[:3].sum() / 3
                    new_pixel = np.broadcast_to(gray, (1, 3))
                    pixel[:3] = new_pixel
            return array
        elif (filter in ['w', 'weight']):
            weight = kwargs['weights']
            for row in array:
                for pixel in row:
                    gray = [(pixel[:3] * weight).sum()]
                    new_pixel = np.broadcast_to(gray, (1, 3))
                    pixel[:3] = new_pixel
            return array
        else:
            return None


if __name__ == "__main__":
    imgProc = ImageProcessor()
    cf = ColorFilter()
    elon = imgProc.load("../elon_canaGAN.png")
    # imgProc.display(elon)

    invertedImage = cf.invert(elon)
    imgProc.display(invertedImage)

    invertedImage = cf.to_blue(elon)
    imgProc.display(invertedImage)

    invertedImage = cf.to_green(elon)
    imgProc.display(invertedImage)

    invertedImage = cf.to_red(elon)
    imgProc.display(invertedImage)

    invertedImage = cf.to_celluloid(elon)
    imgProc.display(invertedImage)

    invertedImage = cf.to_grayscale(elon, 'w', weights=[1.0, 0.0, 0.0])
    imgProc.display(invertedImage)

    invertedImage = cf.to_grayscale(elon, 'm')
    imgProc.display(invertedImage)
