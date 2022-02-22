import numpy as np

##esercizio 1
def presta_libri(title):

    elenco_disponibili = {"Farenheit 451": 10, "Zibaldone": 7, "Aristotle's Metaphysics": 5, "L'Alchimista": 1, "Harry Potter": 2, "Cime tempestose": 1}
    libri_esauriti = {""}
    libri_ordinare = {""}

    if title in elenco_disponibili:
       # print("il libro è presente nell'elenco")

        if  elenco_disponibili[title] == 1:
            elenco_disponibili.pop(title)
            libri_esauriti.add(title)

        else:
            elenco_disponibili[title] -= 1
        #    print("il libro è in prestito")

        return True

    else:
        #print("il libro non è presente nell'elenco")
        libri_ordinare.add(title)

        return False
#------------
print(presta_libri("Zibaldone"))
print(presta_libri("Cime tempestose"))
print(presta_libri("Cuore di tenebra"))

##esercizio 2
def list(a, data):

    if a in data:
        return data.index(a)
    else:
        return False

data = [1, 2, 3, 4, 5, 6]
print(list(5, data))

##esercizio 3
def frequenza_comparsa(stringa):

    w0 = stringa[0]
    count_w0 = stringa.count(w0)
    dict = {w0: count_w0}

    #per l'ist
    bar = '*'
    print(w0, count_w0*bar)

    w1, count_w1 = 0, 0
    for i in range(len(stringa)):
        if stringa[i] in dict:
            continue

        else:
            w1 = stringa[i]
            count_w1 = stringa.count(w1)
            dict1 = {w1: count_w1}
            dict.update(dict1)

            print(w1, count_w1*bar)

    return dict

stringa = "three quarks for muster mark"
dict_f = print(frequenza_comparsa(stringa))

##esercizio 4
def draw():

    a = '#'
    N = input('number:' )

    try:

        return int(N)*a

    except ValueError:

        print('Not valid')
        N = input('number int:' )

        return int(N)*a

print(draw())

##esercizio 5
def rect():

    x, y = '* ', '  '
    Q = input('Play?')
    while Q == 'yes':
        b = int(input('base:' ))
        h = int(input('altezza:' ))
        if b >= 3 and h>= 3:
            print(b*x)
            for i in range(h):
                print(x, y*(b-3), x)
            print(b*x)

            Q = input('Play?')
        else:
            return 'not valid'
    else:
        return 'bye!'

print(rect())

##esercizio 6
def random_game():

    n = int(input('attempt:'))
    r = np.random.randint(1, 10)
    a = float(input('guess the number:'))
    if a > 0 and a%1 == 0:
        if a == r:
            return 'YOU WIN!!'
        else:
            b = input('Continue?')
            if b == 'yes':
                for i in range(n):
                    a = float(input('guess the number:'))
                    if a == r:
                        return 'YOU WIN'
                    else:
                        if i == n-2:
                            return 'you lose'
                        else:
                            print('try again')
            if b == 'no':
                return 'bye!'
    else:
        return 'Not valid'

print(random_game())


















