##esercizio 1
def sec(day, h, min):

    sec = 0
    sec += 60*min
    sec += 3600*h
    sec += 86400*day

    return sec

print(sec(2, 3, 4))

##esercizio 2
def rima(word):

    word1 = 'mare'
    s = len(word1)
    l = len(word)
    if word[l-3:] == word1[s-3:]:
        return 'true'
    else:
        return 'false'

print(rima('andare'), rima('penna'))

##esercizio 3
import numpy as np
def minor(a, b, c):

    l = [a, b, c]
    return np.min(l)

print(minor(10, 54, 3))

##esercizio 4
def f(stringa, parola):

    maiusc = stringa.upper()
    occ = 0
    for i in range(len(stringa)):
        if stringa[i] == 'c':
            occ += 1
        else:
            continue

    l = len(parola)
    for j in range(len(stringa)):
        if stringa[j:j+l] == parola:
            print('yes')
        else:
            continue

    return maiusc, occ

stringa = 'Puoi modificare la tua scelta, in qualsiasi momento, accedendo al pannello delle preferenze'

print(f(stringa, 'momento'))

##esercizio 5
name = 'Luca'
age = 21
print('%s is %d years old.' % (name, age) )

'Natale è  il %d %s' % (25,'Dicembre')

##esercizio 6
a, b = 2, 5.2
sum, mol, sott, div, div_int, mod = a+b, a*b, a-b, a/b, a//b, a%b

l = [1, 2, 3]
m = [0, 4, 6]
sum = l+m


nome1 = 'Maria'
nome2 = 'Giovanna'
nome = nome1 + nome2











