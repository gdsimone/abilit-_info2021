import math
##esercizio 1
nome = 'Gianfranco'
cognome = 'De Simone'
età = 24

print('Buongiorno, mi chiamo', nome, cognome , 'e ho', età, 'anni')

##esercizio 2
n, m = 2,  5
l = m + n
p, q = 3.5, 9.9
r = p*q
z, w = 2 + 6j, 4 + 5j
y = z+y
str1, str2 = 'py', 'thon'
str = str1 + str2
a, b = True, False
c = a or b

s = str(m)
string = str+s
x = complex(l, 7)
comp = x+z

##esercizio 3
def motion(s0, v, dt, a):

    s=0
    if a == 0: #moto rett. unif.
        s = v*dt + s0

    else: #moto unif. acc
        s = 0.5*a*(dt**2) + v*dt + s

    return s

rett_uni = motion(0, 3, 10, 0)
unif_acc = motion(0, 3, 10, 9.81)
print(rett_uni, unif_acc)

##esercizio 4
# nel primo caso viene stampato 3 che è il valore di sum definito fuori dalla funzione, che non è a+b. Nel secondo caso ottengo 200 che è il valore che mi restituisce la funzione che prende in ingresso 100 e 100 e non a = 1, a = 2.

##esercizio 5
from math import pi
def area(l1, l2, r, b, h):

    area = 0
    if l1 != 0 and l2 != 0:
        area = l1*l2
    if r != 0:
        area = pi*r**2
    if b != 0 and h != 0:
        area = 0.5*b*h

    return area

quad = area(2, 2, 0, 0, 0)
rett = area(2, 3, 0, 0, 0)
circ = area(0, 0, 3, 0, 0)
tri = area(0, 0, 0, 5, 4)
print(quad, rett, circ, tri)

##esercizio 6
# dir() è usato per scoprire i nomi definiti all'interno di un modulo. help() ci consente di conoscere la documentazione per ogni funzione. type() ci permette di conoscere il tipo dell'oggetto passato come argomento.

dir(math)

help(math.exp)

k = 4+7j
type(k)



