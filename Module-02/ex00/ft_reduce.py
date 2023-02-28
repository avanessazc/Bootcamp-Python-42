def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    A value, of same type of elements in the iterable parameter.
    None if the iterable can not be used by the function.
    """
    if (not hasattr(iterable, '__iter__') or
            (len(iterable) == 0)):
        return None
    if (len(iterable) > 1 and not callable(function_to_apply)):
        return None

    res = iterable[0]
    for element in iterable[1:]:
        res = function_to_apply(res, element)
    return (res)


if __name__ == "__main__":
    from functools import reduce
    lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
    # lst = [110, 120, 130, 140, 150]

    def sum_function(x, y):
        return (x + y)
    print("----------------FT_REDUCE----------------")
    print(ft_reduce(sum_function, lst))
    try:
        print("------------------REDUCE-----------------")
        print(reduce(sum_function, lst))
    except Exception as e:
        print("None reduce")

    print("----------------FT_REDUCE----------------")
    print(ft_reduce(sum_function, None))
    try:
        print("------------------REDUCE-----------------")
        print(reduce(sum_function, None))
    except Exception as e:
        print("None reduce")

    print("----------------FT_REDUCE----------------")
    print(ft_reduce("None", lst))
    try:
        print("------------------REDUCE-----------------")
        print(reduce("None", lst))
    except Exception as e:
        print("None reduce")

    print("----------------FT_REDUCE----------------")
    print(ft_reduce(None, lst))
    try:
        print("------------------REDUCE-----------------")
        print(reduce(None, lst))
    except Exception as e:
        print("None reduce")
