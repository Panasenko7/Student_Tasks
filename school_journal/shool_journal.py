import requests


GENDER_DETAILS_URL = 'https://api.genderize.io?name='
NATION_URL = 'https://api.nationalize.io?name='


def create_students_list():
    input_total_amount = int(input('Enter total amount of students:'))
    students_list_ = []  # creating an empty list to add all of them

    while len(students_list_) < input_total_amount:
        input_student = input(f'Enter the {len(students_list_) + 1}st student:')
        students_list_.append(input_student)

    return students_list_


def print_details_from_students_list(students_list_):
    for student in students_list_:
        response_from_gender_details_url = requests.get(f'{GENDER_DETAILS_URL}{student}')
        response_dict_from_gender_details_url = response_from_gender_details_url.json()

        response_from_nation_url = requests.get(f'{NATION_URL}{student}')
        response_dict_url_nation = response_from_nation_url.json()

        print(f'{student} gender is probably - {response_dict_from_gender_details_url["gender"]},'
              f' with probability {response_dict_from_gender_details_url["probability"]}, '
              f'nation is {response_dict_url_nation["country"][0]["country_id"]}')


if __name__ == "__main__":
    students_list = create_students_list()
    print_details_from_students_list(students_list)
