def ft_filter(function_to_apply, iterable):
    """Filter the result of function apply to all elements of the iterable.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    An iterable.
    None if the iterable can not be used by the function.
    """

    def generator():
        for element in iterable:
            if (function_to_apply(element) is True):
                yield (element)

    if (not hasattr(iterable, '__iter__') or
            not callable(function_to_apply)):
        return None
    return generator()
    # https://www.programiz.com/python-programming/methods/built-in/filter


if __name__ == "__main__":
    def fct(x):
        if (x % 2 == 0):
            return True
        return False
    arr = range(10)
    print("----------------FT_FILTER----------------")
    print(ft_filter(fct, arr))
    print(*ft_filter(fct, arr))
    print("------------------FILTER-----------------")
    print(filter(fct, arr))
    print(*filter(fct, arr))

    print("----------------FT_FILTER----------------")
    print(ft_filter(fct, 5))
    try:
        print("------------------FILTER-----------------")
        print(filter(fct, 5))
    except Exception as e:
        print("None")

    print("----------------FT_FILTER----------------")
    print(ft_filter("Not function", arr))
    print("------------------FILTER-----------------")
    print(filter("Not function", arr))
