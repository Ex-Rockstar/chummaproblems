# Given two sorted arrays output a merged
# array without duplicates.
# Input
# Array1: [1, 2, 3, 6, 9]
# Array2: [2, 4, 5, 10]
# Output
# Merged Array: [1, 2, 3, 4, 5, 6, 9, 10]



a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=a+b
c=list(set(c))
print(c)
c.sort()
print(c)