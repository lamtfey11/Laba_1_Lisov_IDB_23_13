from classes import Human, Reader, School_Сhild, Student, Club_Member

class Invalid_Key_1_2(Exception):
    pass

def main():
    main_human = ''
    
    ID_1 = 'H_'
    ID_2 = 'R_'
    ID_3 = 'SC_'
    ID_4 = 'S_'
    ID_5 = 'CM_'
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
                        raise Invalid_Key_1_2("Просим прощения, но неправильный ввод. Просим следовать инстуркции, похже мы решим проблему.")
                    else:
                        flag = True
                except Invalid_Key_1_2 as e:
                    print(f"Ошибка: {e}")
            if key == 'New':
                print('New')
            elif key == 'Return':
                print('Return')
             
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