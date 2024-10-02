from classes import Human, Guest


def Human_check_name():
    while True:
        try:
            name = input('Введите своё имя: ')
            if len(name) > 0:
                print('Имя верное')
                return name
            else:
                print("Имя должно иметь хотя бы одну букву.")
        except Exception as n: 
                print(n)

def Human_check_surname():
    while True:
        try:
            surname = input('Введите свою фамилию: ')
            if len(surname) > 0:
                print('Фамилия верная')
                return surname
            else:
                print("Фамилия должна иметь хотя бы одну букву.")
        except Exception as s: 
                print(s)

def Human_check_age():
    while True:
        try:
            age = int(input('Введите свой возраст(если Вам нет 14ти, вы не сможете пользоваться книгами: '))
            if age > 13:
                print('Возраст подходит')
                return age
            else:
                print("Вам должно быть больше 14-ти.")
        except Exception as e: 
            print(e)


name = Human_check_name()
surname = Human_check_surname()
age = Human_check_age()

h = Human(name, surname, age)

print(h.__str__())

name = Human_check_name()
h.set_name(name)
h.get_name()




