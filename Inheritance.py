
class Person():
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    def eat(self):
        print('I am eating')

    def drink(self):
        print('I am drinking')

    def run(self):
        print('I am running')

class Student(Person):
    def __init__(self, name, lastname, age, number):
        super().__init__(name, lastname, age)
        self.number = number
     

class Teacher(Person):
    def __init__(self, name, lastname, age, brans):
        super().__init__(name, lastname, age)
        self.brans = brans
    

p1 = Person("ali", "veli", 32)
s1 = Student("adil","cemal", 9 ,1234)
t1 = Teacher("Fatma","ufuk", 37 , "Ingilizce")

print(f'{p1.name} {p1.lastname} {p1.age} ')
print(f'{s1.name} {s1.lastname} {s1.age} ')
print(f"{t1.name} {t1.lastname} {t1.age} ")

s1.eat()
t1.drink()

s1 = Student("adil","cemal", 1234)
t1 = Teacher("Fatma","ufuk", "Ingilizce")

print(f"{s1.name} {s1.lastname} {s1.number} ")
print(f"{t1.name} {t1.lastname} {t1.brans} ")