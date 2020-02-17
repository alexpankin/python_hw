def my_salary():
    h = float(input("Enter hours: "))
    m = float(input("Enter hourly wages: "))
    b = float(input("Enter bonus: "))
    return h * m + b
print('Размер заработной платы сотавил: ', my_salary())


# from sys import argv
#
# script_name, hours_works, hourly_wages, bonus, salary = argv
#
# print("Enter script: ", script_name)
# print("Enter hours: ", hours_works)
# print("Enter hourly wages: ", hourly_wages)
# print("Enter bonus: ", bonus)
# print("Your salary: ", salary)

