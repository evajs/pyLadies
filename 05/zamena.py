def zamen(retezec, pozice, znak):
    'Zamění znak v řetězci na dané pozici za nový.'
    novy = retezec[:pozice] + znak + retezec[(pozice+1):]
    return novy

print(zamen('pila', 3, 'y'))

