from vector import Vector

if __name__ == "__main__":
    try:
        print("\nColumn vector of shape (n, 1)")
        v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
        print("v1 = ", v1, "Shape", v1.shape)
        v2 = Vector([[0.9], [1.5], [2.5], [3.0]])
        print("v2 = ", v2, "Shape", v2.shape)
        v3 = v1 + v2
        print("v3 = v1 + v2")
        print("v3 = ", v3, "Shape", v3.shape)
        v4 = v1 - v2
        print("v4 = v1 - v2")
        print("v4 = ", v4, "Shape", v4.shape)
    except (Exception) as e:
        print(repr(e))

    try:
        print("\nColumn vector of shape (1, n)")
        v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
        print("v1 = ", v1, "Shape", v1.shape)
        v2 = Vector([[7.0, 10.0, -2.0, 13.0]])
        print("v2 = ", v2, "Shape", v2.shape)
        v3 = v1 + v2
        print("v3 = v1 + v2")
        print("v3 = ", v3, "Shape", v3.shape)
        v4 = v1 - v2
        print("v4 = v1 - v2")
        print("v4 = ", v4, "Shape", v4.shape)
    except (Exception) as e:
        print(repr(e))

    try:
        print("\nColumn vector of shape (n, 1)")
        v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
        print("v1 = ", v1, "Shape", v1.shape)
        v2 = v1 * 5
        print("v2 = v1 * 5")
        print("v2 = ", v2, "Shape", v2.shape)
        v3 = v1 / 2
        print("v3 = v1 / 2")
        print("v3 = ", v3, "Shape", v3.shape)
        print("v4 = v1 / 0")
        v4 = v1 / 0
    except (Exception) as e:
        print(repr(e))

    try:
        print("\nColumn vector of shape (1, n)")
        v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
        print("v1 = ", v1, "Shape", v1.shape)
        v2 = v1 * 5
        print("v2 = v1 * 5")
        print("v2 = ", v2, "Shape", v2.shape)
        print("v4 = 2.0 / v1")
        v4 = 2.0 / v1
    except (Exception) as e:
        print(repr(e))

    try:
        print("\n")
        print("Values: ", Vector([[0.0], [1.0], [2.0], [3.0]]).values)
        v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
        print("Shape: ", v1.shape)
    except (Exception) as e:
        print(repr(e))

    try:
        print("\n")
        v2 = Vector([[0.0, 1.0, 2.0, 3.0]])
        print("v2: ", v2, "Shape: ", v2.shape)
        v3 = v2.T()
        print("v3 = v2.T()")
        print("v3: ", v3, "Shape: ", v3.shape)
    except (Exception) as e:
        print(repr(e))

    try:
        print("\n")
        v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
        v2 = Vector([[2.0], [1.5], [2.25], [4.0]])
        print("v1: ", v1, "Shape: ", v1.shape)
        print("v2: ", v2, "Shape: ", v2.shape)
        print("v1.dot(v2): ", v1.dot(v2))
        print("v1.__repr__():", v1.__repr__())
        print(v1)
    except (Exception) as e:
        print(repr(e))
