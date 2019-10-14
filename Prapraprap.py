import re
import random
#for i in range(10):
#    print(random.randint(0,100))
imiona = []
nazwiska = []
ile = 31
for linijka in open('Imiona.txt','r'):
    imiona.append(linijka)
for i in open('Nazwiska.txt','r'):
    nazwiska.append(i)
def peseluj(pesele,ilosc):
    for i in range(ilosc):
        rok = random.randint(1950,1999)
        miesiac = random.randint(1,12)
        dzien = random.randint(1,29)
        numerek = random.randint(11111,99999)
        rok = str(rok)
        miesiac = str(miesiac)
        dzien = str(dzien)
        numerek = str(numerek)
        if int(dzien)<10:
            dzien = '0' + dzien
        if int(miesiac)<10:
            miesiac = '0' + miesiac
        pesele.append(rok[2:] + miesiac + dzien + numerek)
    return pesele
def listuj(lista):
    #print(lista)
    slowo = ''.join(lista)
    slowo = ''.join(c for c in slowo if c not in ',\n ')
    #print(slowo)
    lista = re.findall('[A-Z][^A-Z]*', slowo)
    #print(lista)
    lista.sort()
    return lista

imiona = listuj(imiona)
#print('Imiona :')
#print(imiona)

nazwiska = listuj(nazwiska)
#print('Nazwiska : ')
#print(nazwiska)

pesele = []
peseluj(pesele,ile)
#print('Pesele : ')
#print(pesele)
numeryT = []
poczta = []
for i in range(ile):
    numeryT.append(str(random.randint(400,999))+'-'+str(random.randint(400,999))+'-'+str(random.randint(400,999)))
    poczta.append(str(random.randint(50,99))+'-'+str(random.randint(111,999)))
print('NumeryTelefonu : ')
print(numeryT)
print('Adresy pocztowe:')
print(poczta)
lista = []

#for i in range(ile):
#    lista.append(i+1)
#print(lista)
dlugoscImiona = len(imiona)
dlugoscNazwiska = len(nazwiska)
dlugoscPesele = len(pesele)
dlugoscNumeryT = len(numeryT)
dlugoscPoczty = len(poczta)
def stworzCzlowieka(lista,i):
    yield ("VALUES" +'('+str(i)+", '"+imiona[random.randint(0,dlugoscImiona-1)] +"', '"+ nazwiska[random.randint(0,dlugoscNazwiska-1)]+"', '"+pesele[random.randint(0,dlugoscPesele-1)] +"', '" + numeryT[random.randint(0,dlugoscNumeryT-1)] +"', '"+ poczta[random.randint(0,dlugoscPoczty-1)]+")")


print(stworzCzlowieka(lista,ile))
for i in range(ile):
    #print('INSERT INTO pracownik(id_pracownik, imie, nazwisko, pesel, telefon, poczta)')
    print('INSERT INTO student(id_student, imie, nazwisko, pesel, telefon, poczta)')
    print(next(stworzCzlowieka(lista,i))+';')
#for i in range(20):
#    print('id_adres '+str(i))
miasta = ['Gdańsk', 'Pruszcz Gdański', 'Sopot', 'Gdynia']
ulice = []
for i in range(ile):
    g=0
    print('INSERT INTO oceny(id_oceny, id_przedmiot, ocena)\n VALUES')
    for j in range(6):

        if g<5:
            print('    (' + str(i) + ',' + str(g) + ',' + str(random.randint(3, 5)) + '),')
        else:
            print('    (' + str(i) + ',' + str(g) + ',' + str(random.randint(3, 5)) + ')')
        g+=1
    print(';')

#for linijka in open('Ulice.txt','r'):
#    ulice.append(linijka)
#print(ulice)
