from test.module_c.utils import VAR_1

def other_fun(var1: int, var2: int) -> str:
    """
    Docstring. more docstring

    :param var1: A number
    :param var2: Another number
    :return:     A string of the numbers
    """
    print(f'called with {var1} and {var2}')

    # Some comment
    result = 5+VAR_1

    # Comment. More comment2. more again.
    print(result)

    # Comment. more comment. some new comment. more more more
    return str(var1 + var2)
