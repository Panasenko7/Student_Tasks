# input_list = ["javelin", "bayraktar", "hello", "banana"]
#
#
# def word(input_list_):
#     return ["PHY" + string[2:] + f' {len(string)}'
#             if string[1] in ['a', 'e', 'o', 'i', 'u', 'y', 'j']
#             else "PHY" + string[1:] + len(string) for string in input_list_]
#
#
# print(word(input_list))


input_list = ["kawabunga", "metro2013", "moon", "orange"]


def modify_list_of_words(input_list_):
    result_list = []

    for word in input_list_:  # проходимся по каждому елементу списка
        modifyed_word = modify_word(word)  # сохраняем результат выполнения функции в переменную

        result_list.append(modifyed_word)  # добавляем переменнуюв список

    return result_list


def modify_word(word_to_modify):  # создаем ф-ю мод врд которая принимает параметр ворд ту модифай
    word_to_return = word_to_modify[1:]  # убираем 1ю букву

    if word_to_return[0] in ("a", "e", "o", "i", "u", "y"):  # если первая буква такая-то
        word_to_return = word_to_return[1:]  # исключаем первую букву

    # добавляем шва к слову прогнанному по условиям функции, пробел и длинна каждого прогнанного слова
    word_to_return = 'Shwa' + word_to_return + ' ' + f' {len(word_to_modify)}'

    return word_to_return  # возвращаем результат получивш слова


# переменная в которой складываем результат выполнения функции можифай лист (инпут - параметр который передаем)
final = modify_list_of_words(input_list)


print(final)
