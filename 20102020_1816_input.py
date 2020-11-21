numer1 = input('numer 1: ')
numer2 = input('numer 2: ')

decyzja = input('wpisz decyzje: ')

if decyzja == 'dodaj' :
    numer3 = int(numer1) + int(numer2)
elif decyzja == 'odejmij':
    numer3 = int(numer1) - int(numer2)
else:
    numer3 = 0

print(numer3)
