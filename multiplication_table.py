list_ = []

for index in range(1, 11):
    list_.append([])

    for index_2 in range(1, 11):
        str_to_append = str(index_2 * index)
        str_to_append = f'{str_to_append: >3}'

        list_[-1].append(str_to_append)

for line in list_:
    print(' '.join(line))

