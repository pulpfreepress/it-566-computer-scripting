import person
import student
import json

def main():
    p1 = person.Person('Rick', 'Warren', 'Miller')
    print(p1)

    p_list = [p1]
    print(p_list)

    s1 = student.Student('Steve', 'Jason', 'Harvey', '12234', 'Computer Science')
    student_dict = {'Steve': s1, 'Rick': p1}

    print(student_dict)

    print(json.dumps(p1, cls=person.PersonJsonEncoder))
    print(json.dumps(s1, cls=student.StudentJsonEncoder))
    print(p1.to_json())


if __name__ == '__main__':
    main()