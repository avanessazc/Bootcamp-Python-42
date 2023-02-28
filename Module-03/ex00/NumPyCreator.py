import numpy as np


class NumPyCreator:

    @staticmethod
    def __check_if_simple_or_nested(array: list or tuple, dtype: type) -> bool:
        if (not isinstance(array, dtype)):
            return False
        # All the element of the array are dtype
        size = None
        for element in array:
            if (not hasattr(element, '__iter__')):
                continue
            if (size is None):
                size = len(element)
            elif (len(element) != size):  # check that all elements have the same size
                return False
        return True

    @staticmethod
    def __check_the_shape(shape) -> bool:
        if (not (isinstance(shape, tuple) and len(shape) == 2 and
                all([(isinstance(obj, int) and obj >= 0) for obj in shape]))):
            return False
        return True

    def from_list(self, lst, dtype=None):
        '''takes a list or nested lists and returns its corresponding
Numpy array'''
        if (not NumPyCreator.__check_if_simple_or_nested(lst, list)):
            return None
        numpy_array = None
        if (dtype is None):
            numpy_array = np.asarray(lst)
        else:
            try:
                numpy_array = np.asarray(lst).astype(dtype)
            except Exception:
                return None
        return (numpy_array)

    def from_tuple(self, tpl, dtype=None):
        '''takes a tuple or nested tuples and returns its corresponding Numpy array.'''
        if (not NumPyCreator.__check_if_simple_or_nested(tpl, tuple)):
            return None
        numpy_array = None
        if (dtype is None):
            numpy_array = np.asarray(tpl)
        else:
            try:
                numpy_array = np.asarray(tpl).astype(dtype)
            except Exception:
                return None
        return (numpy_array)

    def from_iterable(self, itr, dtype=None):
        '''takes an iterable and returns an array which contains
all its elements.'''
        if (not hasattr(itr, '__iter__')):
            return None
        value = list(itr)
        if (len(value) == 0):
            return (np.array([]))
        dtype = type(value[0])
        if (not all([isinstance(obj, dtype) for obj in value])):
            return None
        numpy_array = None
        if (dtype is None):
            numpy_array = np.array(value)
        else:
            try:
                numpy_array = np.array(value).astype(dtype)
            except Exception:
                return None
        return (numpy_array)

    def from_shape(self, shape, value=0, dtype=None):
        '''The first argument is a tuple which specifies the shape of the array, and the second
argument specifies the value of the elements.'''
        if (not (NumPyCreator.__check_the_shape(shape))):
            return None
        if (not (isinstance(value, int) and value >= 0)):
            return None
        numpy_array = None
        if (dtype is None):
            numpy_array = np.full(shape, value)
        else:
            try:
                numpy_array = np.full(shape, value).astype(dtype)
            except Exception:
                return None
        return (numpy_array)

    def random(self, shape, dtype=None):
        if not (NumPyCreator.__check_the_shape(shape)):
            return None
        numpy_array = None
        if (dtype is None):
            numpy_array = np.random.random(shape)
        else:
            try:
                numpy_array = np.random.random(shape).astype(dtype)
            except Exception:
                return None
        return (numpy_array)

    def identity(self, n, dtype=None):
        if not (isinstance(n, int) and n >= 0):
            return None
        numpy_array = None
        if (dtype is None):
            numpy_array = np.eye(n)
        else:
            try:
                numpy_array = np.eye(n).astype(dtype)
            except Exception:
                return None
        # return (np.identity(n))
        return (numpy_array)


if __name__ == "__main__":
    npc = NumPyCreator()

    print(npc.from_list([[1,2,3],[6,3,4]]))
    print("\n")
    print(npc.from_list([[1, 2, 3], [6, 4]]))
    print("\n")
    print(npc.from_list([[1, 2, 3], ['a', 'b', 'c'], [6, 4, 7]]))
    print("\n")
    print(npc.from_list(((1, 2), (3, 4))))
    print("\n")
    print(npc.from_tuple((6, "b", "c")))
    print("\n")
    print(npc.from_tuple(["a", "b", "c"]))
    print("\n")
    print(npc.from_iterable(range(5)))
    print("\n")
    shape = (3, 5)
    print(npc.from_shape(shape))
    print("\n")
    print(npc.random(shape))
    print("\n")
    print(npc.identity(4))

    # print(npc.from_list([[1, 2, 3], [6, 3, 4]], float))
    # print("\n")
    # print(npc.from_list([[1, 2, 3], [6, 4]], float))
    # print("\n")
    # print(npc.from_list([[1, 2, 3], ['a', 'b', 'c'], [6, 4, 7]], float))
    # print("\n")
    # print(npc.from_list(((1, 2), (3, 4)), float))
    # print("\n")
    # print(npc.from_tuple((6, "b", "c"), str))
    # print("\n")
    # print(npc.from_tuple(["a", "b", "c"], float))
    # print("\n")
    # print(npc.from_iterable(range(5), float))
    # print("\n")
    # shape = (3, 5)
    # print(npc.from_shape(shape, dtype=float))
    # print("\n")
    # print(npc.random(shape, float))
    # print("\n")
    # print(npc.identity(4, float))
