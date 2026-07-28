
arr = [5, 1, 3, 4]

a = [9, 7, 6, 5, 4, 3, 2, 1, 8]

#optimal Solution

n = len(arr) + 1

expected_sum_of_arr = (n*(n+1))//2
sum_of_arr = ((n-1)*(n))//2
Missing_number = expected_sum_of_arr - sum_of_arr
print("OPTIMAL SOL",Missing_number)
print()









n = len(arr) + 1
for i in range(1,n + 1):
    print(i)



print()

## Brute Force Solution
n = len(a) + 1
for i in range(1, n + 1):
    if i not in a:
        print(i)





#My attempt
# ar = [12, 11, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# max = float('-inf')
# min = float("+inf")
# for i in range(len(ar)):
#     if ar[i] > max:
#         max = ar[i]
#     if ar[i] < min:
#         min = ar[i]
# fond = False
# for i in range(int(min), int(max)+1):
#     if i not in ar:
#         print(i)
#         fond = True
#         break
# if not fond:
#     print(max+1)
