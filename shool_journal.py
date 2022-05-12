input_total_amount = input('Enter total amount of students:')
input_total_amount = int(input_total_amount)  # asking/entering total amount of people
students_list_ = []  # creating an empty list to add all of them


for student in range(0, input_total_amount):
    input_student = input('Enter the' + f' {len(students_list_)}st ' + 'student:')
    input_student = str(input_student)  # asking/entering each current student
    students_list_.append(str(input_student))


print('You have entered all of them. Here they are:')
print(students_list_)
