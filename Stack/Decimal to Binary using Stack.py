number = 10
remainder = []
while number > 0:
    if number % 2 == 0:

        remainder.insert(0,0)
    else:
        print(number)
        remainder.insert(0,1)

    number = number//2
print(remainder)
while remainder:
    print(remainder.pop())