import xml_job
import json_job

from classes import Human, Reader, School_Сhild, Student, Club_Member

class Invalid_Key_1_2(Exception):
    pass

def Human_job(ID, list_Human):
    index = int(ID[2:])
    
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

    if file_json_xml == 'json':
        file_name = 'data.json'
        data = json_job.start_json(file_name)
        handler = json_job
    elif file_json_xml == 'xml':
        file_name = 'data.xml'
        data = xml_job.start_xml(file_name)
        handler = xml_job
    
    key = ''
    print('Гость имеет такие функции:')
    while key != '3':
        print('1. Взять книгу для чтения в зале.')
        print('2. Удалить свою историю.')
        print('3. Выйти в меню.')
        flag = False
        while flag != True:
            key = input('Введите 1, 2 или 3: ')
            try:
                if key != '1' and key != '2' and key != '3':
                    raise Invalid_Key_1_2("Просим прощения, но неправильный ввод. Просим следовать инстуркции!")
                else:
                    flag = True
            except Invalid_Key_1_2 as e:
                print(f"Ошибка: {e}")

        if key == '1':
            handler.add_human(data, list_Human[index])
            if file_json_xml == 'json':
                handler.save_json(data, file_name)
            else:

                handler.save_to_xml(data, 'data.xml')
        if key == '2':
            handler.delete_human(data, ID)
            if file_json_xml == 'json':
                handler.save_json(data, file_name)
            else:
                handler.save_to_xml(data, 'data.xml')



    


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
        print('3. Ученик школы(человек с ID  на SC_). Вам должно быть от 6 до 18 лет и вы сможете брать книги с таким возрастным ограничением.')
        print('4. Студент вуза(человек с ID  на S_). Вам должно быть от 18 до 27 лет и вы сможете брать книги с таким возрастным ограничением.')
        print('5. Вы хотите быть участником литературного клуба(человек с ID CM_). Вы работаете только в зале.')
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

                    Human_job(ID, list_Human)

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
                        
                        Human_job(index, list_Human)

                        flag = False
  
        #elif main_human == '2':
            
        #elif main_human == '3':

        #elif main_human == '4':

        #elif main_human == '5':

        elif main_human == '6':
            return 'end'
        else:
            print('Просим извинения, но такого номера действия не существует.')



print('Здраствуйте! Это приложение для библиотеки имени Кучуева Вадима Анатольевича.', 'Напишите "Enter", если Вы хотите воспользоваться нашим приложением.', 'Напишите "End", если хотите завершить приём.', 'При других вариантах Вы, к сожалению, не сможете воспользоваться нашим приложением.', 'Желаем Вам удачи!', sep = '\n')
main_on_off = ''
while main_on_off != 'end':
    main_on_off = input('Введите "Enter" или "End": ').lower()
    if main_on_off == 'enter':
        main_on_off = main()