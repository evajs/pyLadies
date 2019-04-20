# def obsah_elipsy(poloosa_a, poloosa_b):
#     "Vrátí obsah elipsy se zadanými poloosami"
#     from math import pi
#     return poloosa_a* poloosa_b * pi
#
# print(obsah_elipsy(2, 3))

from math import pi

def obsah_elipsy(a, b):
    return pi * a * b

print('Obsah elipsy s osami 3 cm a 5 cm je', obsah_elipsy(3, 5), 'cm2')