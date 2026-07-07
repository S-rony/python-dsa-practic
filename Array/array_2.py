from numpy import array

from array import *

val = array("i",[])
n = int(input("Enter a number: "))

for i in range(0, n):
    val.append(i)
    print(val[i])

i = val.index(3)
print(i,"hghg")