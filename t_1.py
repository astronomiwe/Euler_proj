#  Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
num_summary = sum([x for x in range(1, 1000) if x % 3 == 0 or x % 5 == 0])
print(num_summary)
