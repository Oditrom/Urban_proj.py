#Получилось громоздко, но как понял - так и написал, буду рад увидеть ваши комментарии
calls = 0

def string_info():
    a = input('Веедите строку: ')
    b = len(a),a.upper(),a.lower()
    print(b)
    global calls
    calls += 1  
 
def is_contains():
    flag = False
    list_to_search = []
    string = input('Введите строку: ')
    b = int(input('Ведите длину списка: '))
    for i in range(b):   
        list_to_search.append(input('Введите элемент списка: '))
    a = string.lower()
    for _ in list_to_search:
        if a in _.lower() :
            flag = True
    print(flag)
    global calls
    calls += 1

def count_calls():
    flag = True
    while True:
        choice = int(input('1 - string_info, 2 - is_contains, 3 - exit '))
        if choice == 1:
            string_info()
        elif choice == 2:
                is_contains()
        elif choice == 3:
            print(calls)
            flag = False
count_calls()                  