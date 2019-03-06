def other_fun(var1: int, var2: int) -> str:
    """
    Docstring. more docstring

    :param var1: A number
    :param var2: Another number
    :return:     A string of the numbers
    """
    print(f'called with {var1} and {var2}')

    # Some comment
    result = 5+5
    print(result)

    return str(var1 + var2)
