print('Obliczenie sredniej arytmetycznej dwoch liczb')

# WEJSCIE
print('Wprowadz dane wejsciowe: ')
a = float(input('Wprowadz wartosc pierwszej liczby'))
b = float(input('Wprowadz wartosc drugiej liczby'))

# PRZETWARZANIE
if b != 0:
srednia = float(a / b)
print('Srednia wynosi: %f' % srednia)
else:
print('Nie dziel przez 0')
