#человек
class Human:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
        self.status = 'Book in Hool.'

    def back_to_file(self):
        return {
            "name": self.name,
            "ID": self.ID,
            "Status": self.status
        }

#читатель
class Reader(Human):
    def __init__(self, name, ID, age):
        super().__init__(name, ID)  
        self.age = age

    def back_to_file(self):
        self.status = 'Hool'
        reader = super().back_to_file() 
        reader.update({
            "age": self.age
        })
        return reader
    
    def back_to_file_1(self):
        self.status = 'Home'
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
        self.status = 'Hool'
        school_c = super().back_to_file() 
        school_c.update({
            "age": self.age,
            "school": self.school
        })
        return school_c
    
    def back_to_file_1(self):
        self.status = 'Home'
        school_c = super().back_to_file() 
        school_c.update({
            "age": self.age,
            "school": self.school
        })
        return school_c

#студент вуза
class Student(Human):
    def __init__(self, name, ID, age, university):
        super().__init__(name, ID)  
        self.age = age
        self.university = university

    def back_to_file(self):
        self.status = 'Hool'
        student = super().back_to_file() 
        student.update({
            "age": self.age,
            "university": self.university
        })
        return student
    
    def back_to_file_1(self):
        self.status = 'Home'
        student = super().back_to_file() 
        student.update({
            "age": self.age,
            "university": self.university
        })
        return student

#участник читательского клуба
class Club_Member(Human):
    def __init__(self, name, ID, age, club):
        super().__init__(name, ID)  
        self.age = age
        self.club = club
    
    def back_to_file(self):
        self.status = 'Club'
        club_m = super().back_to_file() 
        club_m.update({
            "age": self.age,
            "club": self.club
        })
        return club_m

#компьтерный зал
class Computer_Hool(Human):
    def __init__(self, name, ID, age):
        super().__init__(name, ID)  
        self.age = age

    def back_to_file(self):
        self.status = 'Computer_Hool'
        computer_h = super().back_to_file() 
        computer_h.update({
            "age": self.age
        })
        return computer_h

#подарочный аккаунт
class Gift(Human):
    def __init__(self, name, ID):
        super().__init__(name, ID)  
        self.book = ''

    def back_to_file(self):
        self.status = 'GIFT'
        computer_g = super().back_to_file() 
        computer_g.update({
            "Book": self.book
        })
        return computer_g
    
    def set_book(self, book):
        self.book = book

#aккаунт библиотекаря    
class Bibliotekar():
    def __init__(self):
        self.password = '1234'

    def get_password(self):
        return self.password
    
class Book():
    def __init__(self, name):
        self.name = name
    
    def back_to_file(self):
        return {
            "name": self.name,
        }