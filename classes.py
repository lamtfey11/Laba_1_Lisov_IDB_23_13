#человек
class Human:
    def __init__(self, name, count):
        self.name = name
        self.count = count

    def print(self):
        print(f'Имя гостя {self.name} и его ID: {self.count}')

#читатель
class Reader(Human):
    def __init__(self, name, count, age):
        super().__init__(name, count)  
        self.age = age

#ученик школы
class School_Сhild(Human):
    def __init__(self, name, count, age, school):
        super().__init__(name, count)  
        self.age = age
        self.school = school

#студент вуза
class Student(Human):
    def __init__(self, name, count, age, university):
        super().__init__(name, count)  
        self.age = age
        self.university = university

#участник читательского клуба
class Club_Member(Human):
    def __init__(self, name, count, age, club):
        super().__init__(name, count)  
        self.age = age
        self.club = club