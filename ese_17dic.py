import math
import numpy as np

##list
a = range(1, 20, 2)
print(a, len(a))

b = a[3: 7]
print(b)

list1 = [1, 3, 5, 7, 9]
list2 = [0, 2, 4, 6, 8, 10]
list = list1 + list2
print(list)

#reverse list
list.reverse()
print(list)

l = [1,2]
l2 = ['a','b']
l3 = [4,5]
f = [(e1,e2,e3) for e1 in l for e2 in l2 for e3 in l3]
print(f)


def op_list(a, b, length):

    # a e b estremi dell'intervallo
    list = np.random.randint(a, b, length) #genera una lista random di interi
    M, m = max(list), min(list)
    mu, sigma = np.mean(list), np.var(list)

    return M, m, mu, sigma

M, m, mu, sigma = op_list(0, 1000, 100)
print('max:', M, 'min:', m, 'mean value:', mu, 'dev stand:', np.sqrt(sigma))

##time
import time
p = [i for i in range(100000000)]
p = [i for i in range(1000000)]
T1 = time.clock()
s = q + p
T2 = time.clock()
print('execution time:' , T2-T1, 's=', s)
T3 = time.clock()
q.extend(p)
T4 = time.clock()
print('extend execution time:', T4-T3 , 's=', s)



##tuple
def op_tuple(tup1, tup2):

    L = len(tup1)
    M, m = max(tup1), min(tup1)
    tup = tup1 + tup2

    return M, m, L, tup

tup1 = (1, 3, 5)
tup2 = (2, 4, 6)
M_tup, m_tup, L_tup, tup = op_tuple(tup1, tup2)
print('max:', M_tup, 'min:', m_tup, 'length:', L_tup)
print('sum tup:', tup)


##dict
def op_dict(dict1, dict2):

    return

s = {'abc','def',1,2,3,'ghi'}
s.add(4)
s.update(('lmn',5))
print(s)
