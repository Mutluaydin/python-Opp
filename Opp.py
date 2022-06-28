
class Person:
    # class attributes
    address = "no information"
    
    # constructor
    def __init__(self, name, year):
        
        # object attributes
        self.name = name
        self.year = year
    
    # instance methods
    def calculateAge(self):
        return 2022 - self.year

p1 = Person("ali", 1989)
p2 = Person("ahmet", 1984)

print(f"p1 : name: {p1.name} year: {p1.year} ")
print(f"p2 : name: {p2.name} year: {p2.year} ") 

p1.name = "hasan"
p1.address = "Bern"

print(f"p1 : name: {p1.name} year: {p1.year} address:{p1.address} ")
print(f"p2 : name: {p2.name} year: {p2.year} address:{p2.address} ") 

print(f"p1 : name: {p1.name} Age: {p1.calculateAge()} ")
print(f"p2 : name: {p2.name} Age: {p2.calculateAge()} ") 