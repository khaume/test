from module_a import my_fun

def main():
    print('in the main method')

    result = my_fun(10, 5)

    print(f'The result was {result}')

if __name__ == '__main__':
    main()