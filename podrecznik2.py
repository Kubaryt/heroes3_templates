# SKRYPT POZWALAJACY NA OBLICZENIE POLA I OBWODU PROSTOKATA

print('Obliczenie pola i obwodu prostokata.')

# WEJSCIE
print('Dane wejsciowe:')
a = float(input('Podaj dlugosc pierwszego boku: '))
b = float(input('Podaj dlugosc drugiego boku: '))

# PRZETWARZANIE
p = a * b
o = 2 * a + 2 * b

# WYJSCIE
print('Wyniki: ')
print('Pole prostokata wynosi: %f, a obwod: %f' % (p,o))