symbols = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', ' ', '.', ',', '—', '!']

# Закодированное сообщение
encoded_symbols = [18, 38, 46, 62, 66, 50, 33, 41, 66, 49, 48, 38, 58, 62, 68, 66, 48, 37, 42, 47, 66, 50, 33, 41, 66, 49, 48, 51, 49, 42, 67]

# Раскодированное сообщение
decoded_message = ''
for i in range(len(encoded_symbols)):
    decoded_message += f'{symbols[encoded_symbols[i]]}'
print(decoded_message)


expected_users = 1000

users_by_day = [817, 1370, 752, 1247, 681, 1120, 915, 1281, 875, 1341, 757, 610, 812, 1170, 769, 1261, 845, 1289, 515,
                1247, 845, 1311, 741, 1239, 812, 638, 877, 1242, 1159, 1372]

all_u = 0
max_u = 0
min_u = users_by_day[0]

for i in range(0, len(users_by_day)):
    print('посещаемость в день', i + 1, users_by_day[i])
    all_u += users_by_day[i]

    if max_u < users_by_day[i]:
        max_u = users_by_day[i]
    elif min_u > users_by_day[i]:
        min_u = users_by_day[i]


middle_u = all_u/len(users_by_day)

print('Минимальное значение:', min_u)
print('Максимальное значение:', max_u)
print('Среднее значение:', middle_u)
