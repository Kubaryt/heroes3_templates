print('Obliczenie pola i obwodu prostokata')

a = int(input('Podaj dlugosc pierwszego boku: '))
b = int(input('Podaj dlugosc drugiego boku: '))

p = a * b
o = 2 * a + 2 * b

print('Pole prostokata wynosi: %d, a obwod: %d' % (p, o))