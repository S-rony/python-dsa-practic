from numpy import *
val = array([1,2,3,4,5])
val_one = array([1,2,3,4.5,5])
val_two = array([1, 2, "a",4,5])

for i in range(0,len(val)):
    # val.append(i)
    print(val[i], end = " ")
print()
for i in range(0, len(val)):
        # val.append(i)
    print(val_one[i], end=" ")
print()
for i in range(0, len(val)):
        # val.append(i)
    print(val_two[i], end=" ")
