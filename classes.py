#человек
class Human:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
        self.status = ''

    def back_to_file(self):
        return {
            "name": self.name,
            "ID": self.ID,
            "Book_in_Holl.": self.status
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
        club_m = super().back_to_file() 
        club_m.update({
            "age": self.age,
            "club": self.club
        })
        return club_m