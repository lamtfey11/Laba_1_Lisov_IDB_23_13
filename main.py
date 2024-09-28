class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    
    def print(self):
        return name 
    
    

def Human_check():
    while True:
        try:
            value = int(input('Введите свой возраст(если Вам нет 14ти, вы не сможете пользоваться книгами: )'))
            if value > 13:
                return value
            else:
                print("Вам должно быть больше 14-ти.")
        except Exception as e: 
            print(e)
    return value
        

name, surname = input('Напиши своё имя '), input('Напиши свою фамилию ') 
age = Human_check()
h1 = Human(name, surname, age)
print(h1.print())
