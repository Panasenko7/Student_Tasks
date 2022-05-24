import requests


GENDER_DETAILS_URL = 'https://api.genderize.io?name='
NATION_URL = 'https://api.nationalize.io?name='


def divide_lists_by_ten(input_list):
    result_list = [[]]

    for element in input_list:
        if len(result_list[-1]) <= 10:
            result_list[-1].append(element)
        else:
            result_list.append([])
            result_list[-1].append(element)

    return result_list


def create_students_list():
    input_total_amount = int(input('Enter total amount of students:'))
    student_list = []  # creating an empty list to add all of them

    while len(student_list) < input_total_amount:
        input_student = input(f'Enter the {len(student_list) + 1}st student:')
        student_list.append(input_student)

    return student_list


def print_details_from_students_list(students_list_):
    new_gender_details_list = []

    for student in students_list_:
        response_from_gender_details_url = requests.get(f'{GENDER_DETAILS_URL}{student}')
        response_dict_from_gender_details_url = response_from_gender_details_url.json()
        new_gender_details_list.append(response_dict_from_gender_details_url)

    divided_list = divide_lists_by_ten(input_list=students_list_)

    for student_chunk in divided_list:
        url_with_ten_students = NATION_URL + '&name[]='.join(student_chunk)
        response_from_nation_url = requests.get(url=url_with_ten_students)
        response_list_url_nation = response_from_nation_url.json()

    for gender_info, country_info in zip(new_gender_details_list, response_list_url_nation):
        print(f'Name is {gender_info["name"]}')
        print(f'Gender is {gender_info["gender"]}')
        if country_info["country"]:
            print(f'Country is {country_info["country"]}')
        else:
            print('country unknown')


if __name__ == "__main__":
    students_list = create_students_list()
    print_details_from_students_list(students_list)
