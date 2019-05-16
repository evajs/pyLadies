class Zviratko:
    def __init__(self, jmeno_str):
        self.jmeno = jmeno_str
        self.zvuk = 'not defined'

    def snez(self, jidlo):
        '''
        :param jidlo: co sni
        :return: nic
        vypise, kdo co snedl a ze mu to sne
        '''
        print('{}: Mňam, {} je dobré.'.format(self.jmeno, jidlo))

    def udelej_zvuk(self):
        print(self.zvuk)



class Kotatko(Zviratko):
    def __init__(self, jmeno):
        super().__init__(jmeno)
        self.zvuk = 'Mňau.'

    def snez(self, jidlo):
        print('{} na {} chvili zira.'.format(self.jmeno, jidlo))
        super().snez(jidlo)


class Stenatko(Zviratko):
    def __init__(self, jmeno):
        super().__init__(jmeno)
        self.zvuk = 'Haf.'

k1= Kotatko('Micka')
p1 = Stenatko('Adina')

zviratka = [k1,p1]

for zviratko in zviratka:
    print(zviratko.jmeno)
    zviratko.snez('mleko')
    zviratko.udelej_zvuk()

# k1.snez('ryba')
# p1.snez('kost')

