#человек
class Human:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID

    def back_to_file(self):
        return {
            "name": self.name,
            "ID": self.ID
        }

#читатель
class Reader(Human):
    def __init__(self, name, ID, age):
        super().__init__(name, ID)  
        self.age = age

    def back_to_file(self):
        reader = super().back_to_file() 
        reader.update({
            "age": self.age
        })
        return reader
    
#ученик школы
class School_Сhild(Human):
    def __init__(self, name, ID, age, school):
        super().__init__(name, ID)  
        self.age = age
        self.school = school

    def back_to_file(self):
        reader = super().back_to_file() 
        reader.update({
            "age": self.age
        })
        return reader

#студент вуза
class Student(Human):
    def __init__(self, name, ID, age, university):
        super().__init__(name, ID)  
        self.age = age
        self.university = university

#участник читательского клуба
class Club_Member(Human):
    def __init__(self, name, ID, age, club):
        super().__init__(name, ID)  
        self.age = age
        self.club = club