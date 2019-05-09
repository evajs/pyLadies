class Kotatko:
    def zamnoukej(self):
        print('Mňaaaau!')

    def __init__(self, jmeno_str):
        self.jmeno = jmeno_str

k1 = Kotatko('Micka')
k2 = Kotatko('Mourek')
k1.zamnoukej()
print(k1.jmeno)
print(k2.jmeno)