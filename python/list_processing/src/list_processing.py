

def list_demo():
    number_list = ['a', 2, 'today', 'tomorrow', 'yesterday']
    print(f'First element of number_list is : {str(number_list[0])} ')

    list_2 = [0] * 10
    list_2[0] = 1
    list_2[1] = 2
    list_2[9] = 10
    list_2.append(11)

   
    print(list_2)

    for n in list_2:
        print(f' {n} ', end='')
        
    print()

    list_2[10] = 12

    for n in list_2:
        print(f' {n} ', end='')

    print()

    for n in number_list:
        print(f' {n} ', end='')

    number_list[0] = "Hello, world!"

    print()

    for n in number_list:
        print(f' {n} ', end='')

    first_name = "Rick"

    for c in first_name:
        print(c, end='')

    print()

    number_list.extend(list_2)

    for n in number_list:
        print(f' {n} ', end='')

    print()

    for i in range(len(number_list)):
        number_list[i] = i+1

    print(number_list)

    for i in range(16):
        print(f' {i+1}, ', end='')

    print()

    for n in number_list[6:12]:
        print(f' {n} ', end='')

    print()
    jon = 'Jonathan'

    for c in jon[3:5]:
        print(f' {c} ', end='')

    print()

    print(jon.upper())
