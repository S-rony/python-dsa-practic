

# input = "(()())"
input = ")("
storing = []
valid = True
for i in input:
    if i == "(":
        storing.append(i)
    elif i == ")":
        if len(storing) == 0:
            # print(storing)
            valid = False
            break
        else:
            storing.pop()

        # try:
        #     storing.pop()
        # except IndexError:
        #     print("List is Empty")
        #     break
if len(storing) == 0 and valid == True:
    print("True")
elif valid == False:
    print("False")

