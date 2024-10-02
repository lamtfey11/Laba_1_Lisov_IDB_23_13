
from classes import Human, Reader, School_Сhild, Student, Club_Member

class Invalid_Key_1_2(Exception):
    pass

def Human_job(ID, list = []):
    print('Выбери в какой "базе данных" будешь хранить свою историю: ')
    print('1. json')
    print('2. xml')
    format_file = ''
    flag = False
    while flag != True:
        format_file = input('Напиши 1 или 2: ')
        try:
            if format_file != '1' and format_file != '2':
                raise Invalid_Key_1_2("Просим прощения, но неправильный ввод. Просим следовать инстуркции!")
            else:
                flag = True
        except Invalid_Key_1_2 as e:
            print(f"Ошибка: {e}")
    


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

                    #обращение к функции

                    flag = False
                elif key == 'Return':
                    print('Вы решили вернуться в старый аккаунт.')
                    if len(list_Human) == 0:
                        key = 'New'
                        print('Сейчас вы будете создавать новый аакаунт, так как старых ещё не было.')
                    else:
                        for i in range(len(list_Human)):
                            print(list_Human[i].count, sep = ' ')
                        index = input('Введите номер ID: H_')
                        
                        #обращение к функции 
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