
class Circle():
    pi = 3.14

    def __init__(self, yaricap = 1):
        self.yaricap = yaricap

    def alanHesapla(self):
        return self.pi * (self.yaricap ** 2)

    def cevreHesapla(self):
        return 2 * self.pi * self.yaricap

c1 = Circle()
c2 = Circle(4)

print(f"c1 : Dairenin alani: {c1.alanHesapla()}, Dairenin cevresi: {c1.cevreHesapla()} ")
print(f"c2 : Dairenin alani: {c2.alanHesapla()}, Dairenin cevresi: {c2.cevreHesapla()} ")