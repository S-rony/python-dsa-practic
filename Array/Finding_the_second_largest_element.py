
def second_largest(list):
    max = 0
    second_max = 0
    current_element = 0
    for i in range(len(list)):
        if list[i] > max:
            second_max = max
            max = list[i]
        elif list[i] > second_max and list[i] != max:
            second_max = list[i]

    print(second_max)

second_largest(list=[2,1,4,5,8,10])