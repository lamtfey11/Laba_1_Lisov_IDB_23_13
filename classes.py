#человек
class Human:
    def _init_(self, name, count):
        self.name = name
        self.count = count

#читатель
class Reader(Human):
    def __init__(self, name, count, age):
        super().__init__(name, count)  
        self.age = age