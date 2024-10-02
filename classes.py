class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    
    def __str__(self):
    #__str__ - специальный метод строкового представления объекта
        return f'{self.name} {self.surname} {self.age}'
    
    def set_name(self, n):
        self.name = n

    def set_surname(self, s):
        self.surname = s
    
    def set_age(self, a):
        self.age = a

    def get_name(self):
        print(self.name)

    def get_surname(self):
        print(self.surname)
    
    def get_age(self):
        print(self.age)

class Guest(Human):
    def __init__(self, ID):
        self.ID = ID        
    
