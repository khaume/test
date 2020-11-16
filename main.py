from module_a import my_fun
from module_b.module_b import other_fun

def main():
    print('in the main method..')

    # comment in main
    result = my_fun(10, 10)

    # comment again
    print(f'The result was {result}')

    # comment again again
    print('running module b function')

    # some comment..
    print(other_fun(2, 2))

if __name__ == '__main__':
    main()
