from copy import deepcopy


class Vector:
    '''Vector class
    create vectors and be able to perform \
mathematical operations with them.'''

    @staticmethod
    def check_shape_1_n(array: list) -> bool:
        return all([isinstance(arr, float) for arr in array])

    @staticmethod
    def check_shape_n_1(array: list) -> bool:
        return all([isinstance(arr, list) and
                   len(arr) == 1 and isinstance(arr[0], float)
                   for arr in array])

    def __init__(self, value) -> None:
        if (isinstance(value, (list, int, tuple)) is False):
            raise ValueError("Wrong format of vector. It should be: \
list[float] / list[list[float]] / int / tuple[int]")
        if (isinstance(value, int) and value < 0):
            raise ValueError("Size of range cannot be negative")
        if (isinstance(value, tuple) and
                ((len(value) != 2) or
                 not all([isinstance(obj, int) for obj in value]) or
                 (value[0] >= value[1]))):
            raise ValueError("Wrong format of tuple")

        if (isinstance(value, list)):
            length = len(value)
            if (length == 1):
                if (isinstance(value[0], list)):
                    if (self.check_shape_1_n(value[0])):
                        self.values = deepcopy(value[0])
                        self.shape = (1, len(value[0]))
                    elif (self.check_shape_n_1(value[0])):
                        self.values = deepcopy(value[0])
                        self.shape = (len(value[0]), 1)
                    else:
                        raise ValueError("Wrong Vector list shape")
            elif (length > 1):
                if (self.check_shape_1_n(value)):
                    self.values = deepcopy(value)
                    self.shape = (1, len(value))
                elif (self.check_shape_n_1(value)):
                    self.values = deepcopy(value)
                    self.shape = (len(value), 1)
                else:
                    raise ValueError("Wrong Vector list shape")
        elif (isinstance(value, int)):
            self.values = [[float(nbr)] for nbr in range(value)]
            self.shape = (value, 1)
        elif (isinstance(value, tuple)):
            self.values = [[float(nbr)] for nbr in range(*value)]
            self.shape = (value[1] - value[0], 1)
        else:
            raise Exception("Unexpected error")

    def __repr__(self) -> str:
        txt = f"Values: {self.values} | Shape: {self.shape}"
        return (txt)

    def __str__(self) -> str:
        # https://he-arc.github.io/livre-python/fstrings/index.html
        txt = f"Vector({self.values})"
        return (txt)

    def get_value(self, index: int) -> float or int:
        if (self.shape[0] < index and self.shape[1] < index):
            raise ValueError("index out of bound")
        if (isinstance(self.values[index], float)):
            return self.values[index]
        return self.values[index][0]

    def __add__(self, to_add):
        if (not (isinstance(to_add, Vector) and (to_add.shape == self.shape))):
            raise NotImplementedError("Addition only between \
vectors of same shape")
        tmp = []
        if (self.shape == (1, 1)):
            tmp.append(self.get_value(0) + to_add.get_value(0))
        elif (self.shape[0] > 1):
            for x, y in zip(self.values, to_add.values):
                tmp.append([x[0] + y[0]])
        elif (self.shape[1] > 1):
            for x, y in zip(self.values, to_add.values):
                tmp.append(x + y)
        return Vector([tmp])

    def __radd__(self, to_add):
        # http://www.java2s.com/example/python-book/reusing-add-in-radd.html
        return self.__add__(to_add)

    def __sub__(self, to_sub):
        if not (isinstance(to_sub, Vector) and (to_sub.shape == self.shape)):
            raise NotImplementedError("Subtraction only between \
vectors of same shape")
        tmp = []
        if self.shape == (1, 1):
            tmp.append(self.get_value(0) - to_sub.get_value(0))
        elif self.shape[0] > 1:
            for x, y in zip(self.values, to_sub.values):
                tmp.append([x[0] - y[0]])
        elif (self.shape[1] > 1):
            for x, y in zip(self.values, to_sub.values):
                tmp.append(x - y)
        return Vector([tmp])

    def __rsub__(self, to_sub):
        return self.__sub__(to_sub)

    def __truediv__(self, to_div):
        if not isinstance(to_div, (float, int)):
            raise NotImplementedError("Truediv only with scalars => float/int")
        if float(to_div) == 0.0:
            raise ZeroDivisionError("Division by zero.")
        tmp = []
        if self.shape == (1, 1):
            tmp.append(self.get_value(0) / to_div)
        elif self.shape[0] > 1:
            for x in self.values:
                tmp.append([x[0] / to_div])
        elif (self.shape[1] > 1):
            for x in self.values:
                tmp.append(x / to_div)
        return Vector([tmp])

    def __rtruediv__(self, to_div):
        raise NotImplementedError('Division of a scalar by a \
Vector is not defined here')

    def __mul__(self, to_mul):
        if not isinstance(to_mul, (float, int)):
            raise ValueError("Multiplication only with float/int")
        tmp = []
        if self.shape == (1, 1):
            tmp.append(self.get_value(0) * to_mul)
        elif self.shape[0] > 1:
            for x in self.values:
                tmp.append([x[0] * to_mul])
        elif (self.shape[1] > 1):
            for x in self.values:
                tmp.append(x * to_mul)
        return Vector([tmp])

    def __rmul__(self, to_mul):
        return self.__mul__(to_mul)

    def dot(self, to_dot) -> float or int:
        if (not (isinstance(to_dot, Vector) and
            (self.shape == to_dot.shape or
                 self.shape == to_dot.shape[::-1]))):
            raise NotImplementedError("Vector.dot take a vector \
of same dimension")
        tmp = 0
        length = len(self.values)
        for i in range(length):
            tmp += self.get_value(i) * to_dot.get_value(i)
        return tmp

    def T(self):
        tmp = []
        for x in self.values:
            if isinstance(x, float):
                tmp.append([x])
            else:
                tmp.append(x[0])
        return Vector([tmp])
