


def second_smallest_element(list):
    smallest = float("inf")
    second_smallest = float("inf")
    for ele in list:
        if ele <= smallest:
            second_smallest = smallest
            smallest = ele
        elif ele <= second_smallest and ele != smallest:
            second_smallest = ele
    return second_smallest



print(second_smallest_element(list=[3,7,8,4,2,5]))
