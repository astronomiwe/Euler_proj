# 4 - наибольшее произведение-палиндром, полученное умножением двух трехзначных чисел
# todo два раза делается вывод, исправить
x = 999
y = 999
result = 1
result_str = 'не палиндром'
for i in range(999, 100, -1):
    if result_str == result_str[::-1]:
        print('палиндром - ' + result_str + ' умножили {} * {}'.format(x + 1, y + 1))
        break
    if x>99:
        for j in (999, 100, -1):
            if result_str == result_str[::-1]:
                print('палиндром - ' + result_str + ' умножили {} * {}'.format(x + 1, y + 1))
                break
            if y>99:
                result = x * y
                y -= 1
                result_str = str(result)
            else:
                break
            x -= 1
    else:
        break

