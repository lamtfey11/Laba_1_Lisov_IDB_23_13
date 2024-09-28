class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

def Human_check():
    while True:
        try:
            value = int(input())
            if value > 13:
                return value
            else:
                print("Вам должно быть больше 14ти.")
        
        except Exception as e: 
            print(e)
        


