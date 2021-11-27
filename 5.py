list = [9, 8, 7, 7, 6, 4, 4, 4, 4, 2]
new_number = int(input('Введите новый элемент рейтинга в виде натурального числа - '))
i = 0
for n in list:
    if new_number <= n:
        i += 1
    elif new_number > n:
        break
list.insert(i, float(new_number))
print(list)
