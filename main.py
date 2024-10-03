import xml_job
import json_job
from classes import Human, Reader, School_Сhild, Student, Club_Member

class Invalid_Key_1_2(Exception):
    pass

def age_try(ID):
    if ID[0] == 'R' or ID[0] == 'M':
        flag = False
        while flag != True:
            age = int(input('Введите свой возраст: '))
            try:
                if 4 > age:
                    print('Вам меньше трёх лет.')
                else:
                    flag = True
            except Exception as e:
                print(f"Ошибка: {e}")
    elif ID[0] == 'C':
        flag = False
        while flag != True:
            age = int(input('Введите свой возраст: '))
            try:
                if age < 7 or age > 18:
                    print('Школьником считается человек от 7 до 18.')
                else:
                    flag = True
            except Exception as e:
                print(f"Ошибка: {e}")
    elif ID[0] == 'S':
        flag = False
        while flag != True:
            age = int(input('Введите свой возраст: '))
            try:
                if age < 19 or age > 27:
                    print('Студентом считается человек от 18 до 27.')
                else:
                    flag = True
            except Exception as e:
                print(f"Ошибка: {e}")
    
    return age

def job(ID, list):
    index = int(ID[2:])
    
    file_json_xml = file_name_xml_json()

    if file_json_xml == 'json':
        file_name = 'data.json'
        data = json_job.start_json(file_name)
        handler = json_job
    elif file_json_xml == 'xml':
        file_name = 'data.xml'
        data = xml_job.start_xml(file_name)
        handler = xml_job
    
    key = ''
    print('Список имееющихся функций:')
    while key != '5':
        print('1. Взять книгу для чтения в зале.')
        print('2. Взять книгу для чтения домой.')
        print('3. Удалить свою историю.')
        print('4. Читать книгу в литературном клубе.')
        print('5. Выйти в меню.')
        flag = False
        while flag != True:
            key = input('Введите 1, 2, 3, 4 или 5: ')
            try:
                if key != '1' and key != '2' and key != '3' and key != '4' and key != '5':
                    raise Invalid_Key_1_2("Просим прощения, но неправильный ввод. Просим следовать инстуркции!")
                else:
                    flag = True
            except Invalid_Key_1_2 as e:
                print(f"Ошибка: {e}")

        if key == '1':
            if ID[0] == 'H':
                handler.add_human(data, list[index])
            elif ID[0] == 'R':
                handler.add_reader(data, list[index])
            elif ID[0] == 'C':
                handler.add_school(data, list[index])
            elif ID[0] == 'S':
                handler.add_student(data, list[index])
            else:
                print('Вы не можете пользоваться этой функцией.')

            if file_json_xml == 'json':
                handler.save_json(data, file_name)
            else:
                handler.save_to_xml(data, 'data.xml')
        if key == '2':
            if ID[0] == 'R':
                handler.add_reader_1(data, list[index])
            elif ID[0] == 'C':
                handler.add_school_1(data, list[index])
            elif ID[0] == 'S':
                handler.add_student_1(data, list[index])
            else:
                print('Вы не можете пользоваться этой функцией.')

            if file_json_xml == 'json':
                handler.save_json(data, file_name)
            else:
                handler.save_to_xml(data, 'data.xml')
        if key == '3':    
            if ID[0] == 'H':
                handler.delete_human(data, ID)
            elif ID[0] == 'R':
                handler.delete_reader(data, ID)
            elif ID[0] == 'C':
                handler.delete_school(data, ID)
            elif ID[0] == 'S':
                handler.delete_student(data, ID)
            elif ID[0] == 'M':
                handler.delete_club(data, ID)

            if file_json_xml == 'json':
                handler.save_json(data, file_name)
            else:
                handler.save_to_xml(data, 'data.xml')
        if key == '4':
            if ID[0] == 'M':
                handler.add_club(data, list[index])
            else:
                print('Вы не можете пользоваться этой функцией.')

            if file_json_xml == 'json':
                handler.save_json(data, file_name)
            else:
                handler.save_to_xml(data, 'data.xml')

def file_name_xml_json():
    print("Выберите вид файла, где будет храниться Ваша история, а именно json или xml.")
    file_json_xml = ''
    flag = False

    while flag != True:
        file_json_xml = input('Ввод json или xml: ').lower()
        try:
            if file_json_xml != 'json' and file_json_xml != 'xml':
                raise Invalid_Key_1_2("Просим прощения, но неправильный ввод. Просим следовать инстуркции!")
            else:
                flag = True
        except Invalid_Key_1_2 as e:
            print(f"Ошибка: {e}")
    
    return file_json_xml

def main():
    main_human = ''
    
    count_1 = -1
    count_2 = -1
    count_3 = -1
    count_4 = -1
    count_5 = -1
    list_Human = []
    list_Reader = []
    list_School_Сhild = []
    list_Student = []
    list_Club_Member = []

    while main_human != '6':
        print('Выбирите один из предоставленных вариантов, написав номер действия:')
        print('1. Гость(человек с ID на H_). Вы сможете брать книгу в зале.')
        print('2. Читатель(человек с ID на R_). Вы сможете брать книги в зале и дома.')
        print('3. Ученик школы(человек с ID  на C_). Вам должно быть от 6 до 18 лет и вы сможете брать книги с таким возрастным ограничением.')
        print('4. Студент вуза(человек с ID  на S_). Вам должно быть от 18 до 27 лет и вы сможете брать книги с таким возрастным ограничением.')
        print('5. Вы хотите быть участником литературного клуба(человек с ID M_). Вы работаете только в зале.')
        print('6. Выход')
        
        main_human = input('Введите номер действия: ').strip()

        if main_human == '1':
            print('Напишите "New", если хотите создать новый гостевой аккаунт.', 'Напишите "Return", если хотите вернуться в старый гостевой аккаунт.', sep = '\n')
            
            key = ''
            flag = False
            
            while flag != True:
                key = input('Ввод: ')
                
                try:
                    if key != 'New' and key != 'Return':
                        raise Invalid_Key_1_2("Просим прощения, но неправильный ввод. Просим следовать инстуркции, позже мы решим проблему.")
                    else:
                        flag = True
                except Invalid_Key_1_2 as e:
                    print(f"Ошибка: {e}")
            
            while flag != False:
                if key == 'New':
                    print('Вы решили создать новый аккаунт.')

                    count_1 += 1
                    ID = 'H_' + str(count_1)
                    print(f'Ваш ID: {ID}')
                    name = input('Введите своё имя: ')
                    list_Human.append(Human(name, ID))

                    job(ID, list_Human)

                    flag = False
                elif key == 'Return':
                    print('Вы решили вернуться в старый аккаунт.')
                    if len(list_Human) == 0:
                        key = 'New'
                        print('Сейчас вы будете создавать новый аакаунт, так как старых ещё не было.')
                    else:
                        for i in range(len(list_Human)):
                            print(list_Human[i].ID, sep = ' ')
                        index = 'H_'
                        index += input('Введите номер ID: H_')
                        
                        job(index, list_Human)

                        flag = False
  
        elif main_human == '2':
            print('Напишите "New", если хотите создать новый аккаунт читателя.', 'Напишите "Return", если хотите вернуться в старый аккаунт.', sep = '\n')
            
            key = ''
            flag = False
            
            while flag != True:
                key = input('Ввод: ')
                
                try:
                    if key != 'New' and key != 'Return':
                        raise Invalid_Key_1_2("Просим прощения, но неправильный ввод. Просим следовать инстуркции, позже мы решим проблему.")
                    else:
                        flag = True
                except Invalid_Key_1_2 as e:
                    print(f"Ошибка: {e}")
            
            while flag != False:
                if key == 'New':
                    print('Вы решили создать новый аккаунт.')

                    count_2 += 1
                    ID = 'R_' + str(count_2)
                    print(f'Ваш ID: {ID}')
                    name = input('Введите своё имя: ')
                    age = age_try(ID)
                    list_Reader.append(Reader(name, ID, age))

                    job(ID, list_Reader)

                    flag = False
                elif key == 'Return':
                    print('Вы решили вернуться в старый аккаунт.')
                    if len(list_Reader) == 0:
                        key = 'New'
                        print('Сейчас вы будете создавать новый аакаунт, так как старых ещё не было.')
                    else:
                        for i in range(len(list_Reader)):
                            print(list_Reader[i].ID, sep = ' ')
                        index = 'R_'
                        index += input('Введите номер ID: R_')
                        
                        job(index, list_Reader)

                        flag = False
  
        elif main_human == '3':
            print('Напишите "New", если хотите создать школьный аккаунт.', 'Напишите "Return", если хотите вернуться в старый аккаунт.', sep = '\n')
            
            key = ''
            flag = False
            
            while flag != True:
                key = input('Ввод: ')
                
                try:
                    if key != 'New' and key != 'Return':
                        raise Invalid_Key_1_2("Просим прощения, но неправильный ввод. Просим следовать инстуркции, позже мы решим проблему.")
                    else:
                        flag = True
                except Invalid_Key_1_2 as e:
                    print(f"Ошибка: {e}")
            
            while flag != False:
                if key == 'New':
                    print('Вы решили создать новый аккаунт.')
                    
                    count_3 += 1
                    ID = 'C_' + str(count_3)
                    print(f'Ваш ID: {ID}')
                    name = input('Введите своё имя: ')
                    age = age_try(ID)
                    school = input('Введите место учёбы(школу): ')
                    list_School_Сhild.append(School_Сhild(name, ID, age, school))

                    job(ID, list_School_Сhild)

                    flag = False
                elif key == 'Return':
                    print('Вы решили вернуться в старый аккаунт.')
                    if len(list_School_Сhild) == 0:
                        key = 'New'
                        print('Сейчас вы будете создавать новый аакаунт, так как старых ещё не было.')
                    else:
                        for i in range(len(list_School_Сhild)):
                            print(list_School_Сhild[i].ID, sep = ' ')
                        index = 'C_'
                        index += input('Введите номер ID: C_')
                        
                        job(index, list_School_Сhild)

                        flag = False

        elif main_human == '4':
            print('Напишите "New", если хотите создать студенческий аккаунт.', 'Напишите "Return", если хотите вернуться в старый аккаунт.', sep = '\n')
            
            key = ''
            flag = False
            
            while flag != True:
                key = input('Ввод: ')
                
                try:
                    if key != 'New' and key != 'Return':
                        raise Invalid_Key_1_2("Просим прощения, но неправильный ввод. Просим следовать инстуркции, позже мы решим проблему.")
                    else:
                        flag = True
                except Invalid_Key_1_2 as e:
                    print(f"Ошибка: {e}")
            
            while flag != False:
                if key == 'New':
                    print('Вы решили создать новый аккаунт.')
                    
                    count_4 += 1
                    ID = 'S_' + str(count_4)
                    print(f'Ваш ID: {ID}')
                    name = input('Введите своё имя: ')
                    
                    age = age_try(ID)
                    university = input('Введите место учёбы(вуз): ')
                    list_Student.append(School_Сhild(name, ID, age, university))

                    job(ID, list_Student)

                    flag = False
                elif key == 'Return':
                    print('Вы решили вернуться в старый аккаунт.')
                    if len(list_Student) == 0:
                        key = 'New'
                        print('Сейчас вы будете создавать новый аакаунт, так как старых ещё не было.')
                    else:
                        for i in range(len(list_Student)):
                            print(list_Student[i].ID, sep = ' ')
                        index = 'S_'
                        index += input('Введите номер ID: S_')
                        
                        job(index, list_Student)

                        flag = False

        elif main_human == '5':
            print('Напишите "New", если хотите создать клубный аккаунт.', 'Напишите "Return", если хотите вернуться в старый аккаунт.', sep = '\n')
            
            key = ''
            flag = False
            
            while flag != True:
                key = input('Ввод: ')
                
                try:
                    if key != 'New' and key != 'Return':
                        raise Invalid_Key_1_2("Просим прощения, но неправильный ввод. Просим следовать инстуркции, позже мы решим проблему.")
                    else:
                        flag = True
                except Invalid_Key_1_2 as e:
                    print(f"Ошибка: {e}")
            
            while flag != False:
                if key == 'New':
                    print('Вы решили создать новый аккаунт.')
                    
                    count_5 += 1
                    ID = 'M_' + str(count_5)
                    print(f'Ваш ID: {ID}')
                    name = input('Введите своё имя: ')
                    
                    age = age_try(ID)
                    club = input('Введите название клуба: ')
                    list_Club_Member.append(Club_Member(name, ID, age, club))

                    job(ID, list_Club_Member)

                    flag = False
                elif key == 'Return':
                    print('Вы решили вернуться в старый аккаунт.')
                    if len(list_Club_Member) == 0:
                        key = 'New'
                        print('Сейчас вы будете создавать новый аакаунт, так как старых ещё не было.')
                    else:
                        for i in range(len(list_Club_Member)):
                            print(list_Club_Member[i].ID, sep = ' ')
                        index = 'M_'
                        index += input('Введите номер ID: M_')
                        
                        job(index, list_Club_Member)

                        flag = False

        elif main_human == '6':
            return ''
        else:
            print('Просим извинения, но такого номера действия не существует.')



print('Здраствуйте! Это приложение для библиотеки имени Кучуева Вадима Анатольевича.', 'Напишите "Enter", если Вы хотите воспользоваться нашим приложением.', 'Напишите "End", если хотите завершить приём.', 'При других вариантах Вы, к сожалению, не сможете воспользоваться нашим приложением.', 'Желаем Вам удачи!', sep = '\n')
main_on_off = ''
while main_on_off != 'end':
    main_on_off = input('Введите "Enter" или "End": ').lower()
    if main_on_off == 'enter':
        main_on_off = main()