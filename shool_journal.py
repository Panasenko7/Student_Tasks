import requests


URL = 'https://api.genderize.io?name='

input_total_amount = int(input('Enter total amount of students:'))
# input_total_amount = int(input_total_amount)  # asking/entering total amount of people
students_list_ = []  # creating an empty list to add all of them


# for student_number in range(input_total_amount):
#     input_student = input(f'Enter the {len(students_list_)+1}st student:')
#     # input_student = str(input_student)  # asking/entering each current student
#     # students_list_.append(str(input_student))
#     students_list_.append(input_student)

while len(students_list_) < input_total_amount:
    input_student = input(f'Enter the {len(students_list_) + 1}st student:')
    students_list_.append(input_student)


for student in students_list_:
    response = requests.get(f'{URL}{student}')
    response_dict = response.json()
    print(f'{student} gender is probably {response_dict["gender"]} with probability {response_dict["probability"]}')
print('You have entered all of them. Here they are:')
print(students_list_)
