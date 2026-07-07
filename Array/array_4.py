from numpy import *

val = linspace(10,20,5)
val_one = arange(10,20,2)
for i in range(0, len(val)):
    print(val[i], end= " ")
print()
for i in range(0, len(val_one)):
    print(val_one[i], end = " ")