revenue = int(input('Введите выручку в деньгах: '))
costs = int(input('Введите издержки: '))


if revenue < costs:
    penalty_cost = revenue - costs
    print('Предприятие работает в убыток', '\n', 'Ваш убыток составляет: ', penalty_cost, ' денег', sep='')
elif revenue > costs:
    marg = revenue - costs
    profit_marg = (marg / revenue) * 100
    print('Ваша прибыль сотавляет: ', marg, 'денег')
    print('Рентабельность равна: ', profit_marg, '%')
    pers = int(input('Введите количесто сотрудников: '))
    pers_marg = marg / pers
    print('Прибыль на сотрудника составляет: ', pers_marg, 'денег')
else:
    print('Прибыль предприятия нулевая')
