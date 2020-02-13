def my_calc():
    arg_1 = int(input('Введите делимое: ')),
    arg_2 = int(input('Введите делитель: '))

    try:
        print(arg_1 / arg_2)
    except ZeroDivisionError:
        print('На 0 делить нельзя')
    print('Попробуйте еще раз')

    arg_3 = arg_1 / arg_2
    return arg_3
print(f'Частное: ', round(my_calc(), 2))
