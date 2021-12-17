##Lecture 3
import numpy as np

#----guess number----#
def guess_numb(n):

    list = np.random.randint(0, 100, 50)
    for i in range(len(list)):
        m = list[i]
        if m == n:
            return print('Congratulations! you guessed it')
            break
        else:
            if i == len(list)-1:
                return print('Fail')
            else:
                continue

guess_numb(10)