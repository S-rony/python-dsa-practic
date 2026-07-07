from array import *

val = array("i",[1,2,3,4,5])

# print(val)
# for i in range(0,6):
#     print(i)
# for i in range(len(val)):
#     # print(val[i])
#     print(val.typecode)
#     val.reverse
print(val.typecode)
val.insert(1,50)
val.append(100)
val[3] = 9
copayArray = array(val.typecode,(x*3 for x in val))
copayArray.pop()
copayArray.remove(6)

for i in range(0, len(copayArray)):
    print(copayArray[i],end=" ")



