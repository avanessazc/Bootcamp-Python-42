def ft_map(function_to_apply, iterable):
    """Map the function to all elements of the iterable.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    An iterable.
    None if the iterable can not be used by the function.
    """
    def generator():
        for element in iterable:
            yield (function_to_apply(element))

    if (not hasattr(iterable, '__iter__') or
            not callable(function_to_apply)):
        return None
    return generator()
    # https://www.programiz.com/python-programming/methods/built-in/map


if __name__ == "__main__":
    arr = range(10)
    print("----------------FT_MAP----------------")
    res_ft_map = ft_map(lambda x: x*2, arr)
    arr_list_ft_map = list(res_ft_map)
    print(res_ft_map)
    print(arr_list_ft_map)
    print("------------------MAP-----------------")
    res_map = map(lambda x: x*2, arr)
    arr_list_map = list(res_map)
    print(res_map)
    print(arr_list_map)
    print("\n")

    print("----------------FT_MAP----------------")
    print(ft_map(lambda x: x*2, 5))
    try:
        print("------------------MAP-----------------")
        print(map(lambda x: x*2, 5))
    except Exception as e:
        print("None")
    print("\n")

    print("----------------FT_MAP----------------")
    print(ft_map("Not function", arr))
    print("------------------MAP-----------------")
    print(map("Not function", arr))
