# найти разность между квадратом суммы и суммой квадратов первых 100 нат. чисел

difference = sum([x for x in range(1, 100)]) ** 2 - sum([x ** 2 for x in range(1, 100)])
print(difference)
