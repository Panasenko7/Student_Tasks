# Инвертировать текст
# 1 из 3
# срез строки через степ -1
str_ = "Invert me Please 111"[::-1]
# 2 из 3
# встроенная функция Реверс, метод джоин преобразование в строку
s = "Invert me Please 222"
res = ''.join(reversed(s))
# 3 из 3
# Рекурсия
s1 = "Invert me Please 333"
def reversed(s1):
    if len(s1) == 1:
        return s1
    else:
        return s1[-1] + reversed(s1[:-1])

print("1-->", (str_))
print("2-->", (res))
print("3-->", (reversed(s1)))