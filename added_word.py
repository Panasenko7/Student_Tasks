input_list = ["javelin", "bayraktar", "huilo", "banana"]


def qqq(input_list_):
    return ["Hui" + string[2:] + f'-{len(string)}'
            if string[1] in ['a', 'e', 'o', 'i', 'u', 'y', 'j']
            else "Hui" + string[1:] + len(string) for string in input_list_]


print(qqq(input_list))
