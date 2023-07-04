from person import Person
from student import Student
import json

def main():
    # Need to create instance of Person
    p1 = Person('Rick', 'Warren', 'Miller')
    print(f'p1 = {p1.first_name}')

    s1 = Student('Jonathan', 'J', 'Ashford', '12345', 'Cybersecurity')
    print(f's1.first_name: {s1.first_name} Major: {s1.major}')
    print(f'{s1}')

    s2 = Student('Tony', 'R', 'Nguyen', '23456', 'Cybersecurity')
    print(f'{s2}')

    p2 = Person("Steve", "W", "Smith")

    

    students = [s1, s2, p1]

    for s in students:
        print(f'{s}')

    student_dictionary = {"s1": json.loads(s1.toJSON()), "s2":json.loads(s2.toJSON()) }
    json_string = json.dumps(student_dictionary)
    print(f'{json_string}')

    new_dictionary = json.loads(json_string)
    print(f'{new_dictionary}')

if __name__ == '__main__':
    main()