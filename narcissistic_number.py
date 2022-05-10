# создаём переменную для реультата со значением 0
# проходимся по каждой цифре из числа (число конвертируем в строку чтобі єто сделать)
# каждую цифру возводим в степень длины изначального числа
# добавляем получившуюся хуйню к переменной для результата (** возв в степ).


a_1 = 153
str_to_iterate = str(a_1)
fin_res = 0
for num in str_to_iterate:
    # num **len(str_to_iterate)
    fin_res = fin_res + int(num) ** len(str_to_iterate)

if a_1 == fin_res:
    print('ok')
else:
    print('not ok')


