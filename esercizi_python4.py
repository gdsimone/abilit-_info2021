import numpy as np
import os
##esercizio 1
class point3D():


    def _init_(self):

        x0, y0, z0 = input('x0:'), input('y0:'), input('z0:')
        self.Q = [int(x0), int(y0), int(z0)]

    def dist(self):

        change = input('change coordinates?')

        if change == 'yes' or change == 'si':
            x0, y0, z0 = input('x0:'), input('y0:'), input('z0:')
            self.Q = [int(x0), int(y0), int(z0)]
            P = self.Q

        else:
            P = self.Q

        x1, y1, z1 = int(input('x1:')), int(input('y1:')), int(input('z1:'))

        p = np.power
        d = np.sqrt(p(x1 - P[0] , 2) + p(y1 - P[1] , 2) + p(z1 - P[2] , 2) )

        return d

cl = point3D()
cl._init_()
print(cl.dist())

 ##esercizio 2 e 3
class IG():

    def _init_(self):

        os.chdir('C:/Users/Gianfranco/Desktop/Nuova cartella')
        nome_file = input('Nome file: ') #ex2_data_python_4.txt
        self.x, self.y = np.loadtxt( nome_file, unpack = True)

    def calc_bar(self):

        try:
            x_G = np.mean(self.x)
            y_G = np.mean(self.y)

        except ZeroDivisionError:
            print("division by zero!")

        return x_G, y_G

ig = IG()
ig._init_()
print(ig.calc_bar())

##esercizio 4
class campionato_sportivo():

    def _init_(self):

        os.chdir('C:/Users/Gianfranco/Desktop/Nuova cartella')
        team = list(open( 'serie_a.txt', 'r'))
        for i in range(len(team)-1):
            team[i] = team[i][:-1]

        punti = list(np.loadtxt('punti.txt'))
        for i in range(len(punti)):
            punti[i] = int(punti[i])

        self.classifica = list(zip(team, punti))


    def promoz_retrocess(self):

        #---remove team---

        team, punti = zip(*self.classifica)
        team, punti = list(team), list(punti)
        team_retr = input('Squadra da eliminare: ')

        if team_retr in team:
            ind_del = team.index(team_retr)
            p_del = punti[ind_del]
            team.remove(team_retr)
            punti.remove(p_del)
            self.classifica = list(zip(team, punti))

        else:
            print('Not valid')

        #---add team---
        team_pro = input('Squadra da aggiungere: ')
        if team_pro == 'None' or team_pro == 'Nessuna':
            self.classifica = list(zip(team, punti))

        else:
            punti_pro = int(input('Punti nuova squadra: '))
            team.append(team_pro)
            punti.append(punti_pro)
            self.classifica = list(zip(team, punti))

    def winner_losers(self):

        team, punti = zip(*self.classifica)
        team, punti = list(team), list(punti)

        p_max = np.max(punti)
        win_team = team[punti.index(p_max)]

        p_min = np.min(punti)
        los_team = team[punti.index(p_min)]

        punti.remove(p_min)
        p_min2 = np.min(punti)
        los_team2 = team[punti.index(p_min2)]

        punti.remove(p_min2)
        p_min3 = np.min(punti)
        los_team3 = team[punti.index(p_min3)]


        return 'The winner is:', win_team, 'with points', p_max ,'The losers are:', los_team, los_team2, los_team3 , 'with points respectively', p_min, p_min2, p_min3

cs = campionato_sportivo()
cs._init_()
cs.promoz_retrocess()
print(cs.winner_losers())

##esercizio 5
def scalar(list1, list2):

    result = 0
    if len(list1) == len(list2):
        for i in range(len(list1)):
            x = list1[i] * list2[i]
            result += x

    else:
        raise NameError('vectors must have the same length')

    return result

list1, list2 = [1, 2, 3], [3, 0, 7]
print(scalar(list1, list2))

def matrix_prd(matrix1, matrix2):

    r1, c1 = np.shape(matrix1)
    r2, c2 = np.shape(matrix2)
    result = np.zeros((r1, c2), dtype=int)
    if c1 == r2:
        for i in range(r1):
            row1 = matrix1[i]
            for j in range(c2):
                clm1 = [row[j] for row in matrix2]

                result[i, j] = scalar(row1, clm1)

        return result

    else:
        raise NameError('Matrix product is possible only between matrices n,m x m,p')

m1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
m2 = np.array([[4,2,7],[0,5,0],[1,2,4]])
print(matrix_prd(m1, m2))

##esercizio 6
# la funzione lambda è una funzione anonima che prende in input un set di parametri e ridà l'espressione contenuta nel body. Cioè, nel caso sum10 = lambda a: a+10, la funzione prende in input un numero e restituisce tale numero +10 (sum(5) = 15). Invece, f = lambda animale: animale.capitalize(), converte il primo carattere della stringa 'animale' in maiuscolo, f(animali[0]) = 'Cani'.

mean = lambda x, y: (x+y)/2
print(mean(1, 2))





