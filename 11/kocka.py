class Kocka:
    def __init__(self):
        self.zivoty=9

    def zamnoukej(self):
        print("Mnau")

    def je_ziva(self):
        return self.zivoty> 0

    def uber_zivot(self):
        self.zivoty -=1
        return self.zivoty

    def snez(self,jidlo):
        if not self.je_ziva():
            print('Je zbytecne krmit mrtvou kocku')
            return
        if jidlo=='ryba' and self.zivoty < 9:
            self.zivoty +=1
            print('Mnam, ryba, o zivot vic')
        else:
            print('Mnam')

k1=Kocka()
k1.snez('ryba')
k1.uber_zivot()
k1.snez('kost')
k1.snez('ryba')
