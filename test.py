
# list_one = ["first elem", "second elem","third elem"]
# list_two = ["11", "22", "33"]
#
# result_list = []
# for element in list_one:  # пройтись по всем элеметам списка list_one
#     print(element)  # и напечатать
#
# ###########################################################
# # --------------------------------
# ###########################################################
#
# # вызвать функцию и назначить результат её выполнения переменной
#
# string_to_modify = "modify me pls"
#
#
# def modify_string(input_value):  # задали функцию
#     return input_value + " string modified"
#
#
# modified_string = modify_string(string_to_modify)
#
# print(modified_string)
#
#
# ###########################################################
# # --------------------------------
# ###########################################################
#
# # простись по списку получая не только каждый элемент, но и индекс
#
# for index, list_value in enumerate(list_one):
#     print(f'Index:{index}; Value: {list_value}')
#
# # так можно обращаться к любому списку, который состоит из корtежей (tuple) по два элемента
# # ,типа [(1,2), (1,2), ...]
#
# # соединить два списка попарно, чтобы можнобыло так к ним обращаться - zip()
#
# for list_one_value, list_two_value in zip(list_one, list_two):
#     print(f'1: {list_one_value}; 2: {list_two_value}')
#
# # while loop
#
# a = 0
# while a < 5:
#     print('a <5')
#
#     a = a + 1
#
# #input_total_amount = int(input('Enter total amount of students:'))
# # input_total_amount = int(input_total_amount)  # asking/entering total amount of people
# #students_list_ = []  # creating an empty list to add all of them
#
#
# for student_number in range(input_total_amount):
#     input_student = input(f'Enter the {len(students_list_)+1}st student:')
#     # input_student = str(input_student)  # asking/entering each current student
#     # students_list_.append(str(input_student))
#     students_list_.append(input_student)

