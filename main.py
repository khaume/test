from test.module_a import my_fun
from test.module_b.module_b import other_fun

def main():
    print('in the main method..')

    # comment in main
    result = my_fun(10, 5)

    # comment again
    print(f'The result was {result}')

    # comment again again
    print('running module b function')
    print(other_fun(2, 2))

if __name__ == '__main__':
    main()
