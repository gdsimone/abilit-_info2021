import math
import sys

#Numeric types#

print(sys.maxsize)

print(sys.float_info)

#num base oct, hex, bin
def rapp_base(a):

    return oct(a), hex(a), bin(a)

a=300
string = 'Rappresentazione %d in base:' % (a)
print(string)
print('oct', rapp_base(a)[0])
print('hex', rapp_base(a)[1])
print('bin', rapp_base(a)[2])

r=12+5j # complex
type(r)
s=15
print('Real:', r.real, 'Imag:', r.imag)
print('sum complx + real:',r+s)