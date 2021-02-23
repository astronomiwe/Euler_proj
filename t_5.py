# Какое самое маленькое число делится нацело на все числа от 1 до 20?
i = 20
result = 0
for i in range(20, 11 * 12 * 13 * 14 * 15 * 16 * 17 * 18 * 19 * 20, 20):
    if i % 11 == 0 and i % 12 == 0 and i % 13 == 0 and i % 14 == 0 and i % 15 == 0 and i % 16 == 0 and i % 17 == 0 and i % 18 == 0 and i % 19 == 0 and i % 20 == 0:
        result = i
        print(result)
        break


