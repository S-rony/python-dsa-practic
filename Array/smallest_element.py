def smallest_element(list):
    smallest_element = float("inf")

    for element in list:
        if element <= smallest_element:
            smallest_element = element
    return smallest_element

print(smallest_element(list=[3,5,8,9,1]))