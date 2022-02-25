import matplotlib.pyplot as plt
import numpy as np
import os
##esercizio 1
def ist(data):

    a = '*'
    for i in range(len(data)):
        print(a*data[i])

data = [2, 3, 5, 9, 7, 4]
print(ist(data))
#---
def ist_graf(data):

    plt.figure(1)
    plt.bar(range(len(data)), data, width=0.5)
    plt.show()

ist_graf(data)

##esercizio 2
def stat(anni, T_mu, T_min, T_max, Pioggia):

    #--con numpy
    var_tmin, var_tmax  = np.var(T_min), np.var(T_max)
    dev_tmin, dev_tmax = np.sqrt(var_tmin), np.sqrt(var_tmax)

    plt.figure(2)
    plt.xlabel('anni')
    plt.plot(anni, T_min, color = 'blue', label = 'temperatura min')
    plt.plot(anni, T_max, color = 'orange', label = 'temperatura max')
    plt.legend()
    plt.show()
    return var_tmin, dev_tmin, var_tmax, dev_tmax

os.chdir('C:/Users/Gianfranco/Desktop/Nuova cartella')
file = 'ex2_data_python_5.txt'
anni, T_mu, T_min, T_max, Pioggia = np.loadtxt(file, unpack = True)
print(stat(anni, T_mu, T_min, T_max, Pioggia))

#----var e dev senza numpy---#
def calc_var(array):

    m  = 0
    for i in range(len(array)):
        m += array[i]

    m = m/len(array)

    var = 0
    for j in range(len(array)):
        var += (array[j] - m)**2

    var = var/len(array)

    return var, var**(0.5)

print(calc_var(T_min), calc_var(T_max))

##esercizio 3
a = np.random.randint(20, size = (3, 3))
row, element, centre = a[0], a[2][0], a[1][1]
v = np.random.randint(20, size = 10)
m, n, l = v[1:], v[4:9], v[:-2] #toglie [0], prende da [4] a [8] inclusi, toglie [8] e [9]

b = v # copy by reference (it is the copy of memory area pointer)
b[1] = 33

c = v.copy() #copy by value (a new memori area is crested with the same value)
c[0] = 27

x, y = np.array([1, 3, 6, 8]), np.array([11, 4, 7, 21])
sumxy = x+y
molxy = x*y

##esercizio 4
os.chdir('C:/Users/Gianfranco/Desktop/Nuova cartella')
matrix = np.loadtxt( 'matrix.txt', unpack = True)
autovalori, autovettori = np.linalg.eig(matrix)
print(autovalori, autovettori)

##esercizio 5
def sigmoide(x):

    F = 1/(1+np.exp(-x))

    return F

print(sigmoide(0.458))

##esercizio 6
L = 1000
start1 = time.time()
a, b = np.zeros((L, L)), np.zeros((L, L))
for i in range(L):
    for j in range(L):
        a[i, j] = np.random.randint(0,200)
        b[i, j] = np.random.randint(0,200)

end1 = time.time()
print('tempo con for',end1-start1)

start = time.time()
m1 = np.random.randint(200, size = (L, L))
m2 = np.random.randint(200, size = (L, L))
end = time.time()
print('tempo con numpy', end-start)
