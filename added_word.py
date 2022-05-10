input_list = ["javelin", "bayraktar", "hello", "banana"]


def word(input_list_):
    return ["PHY" + string[2:] + f' {len(string)}'
            if string[1] in ['a', 'e', 'o', 'i', 'u', 'y', 'j']
            else "PHY" + string[1:] + len(string) for string in input_list_]


print(word(input_list))

