string = "hello"
stack = []
for  i in string:
    stack.append(i)
# for i in range(len(stack)):
#     print(stack.pop(),end="")

while stack:
    print(stack.pop(),end= "")

