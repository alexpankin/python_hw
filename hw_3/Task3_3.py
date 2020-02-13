def my_func(par_1, par_2, par_3):
    d = [par_1, par_2, par_3]
    d.remove(min(par_1, par_2, par_3))
    return sum(d)
print(my_func(par_1 = 12, par_2 = 2, par_3 = 8))

# def my_func(*args):
# numbers = []
#
# for i in range(3):
#     number = input("Enter date: ")
#     numbers.append(number)
#     numbers.remove(min(numbers))
#
# print(sum(numbers))
