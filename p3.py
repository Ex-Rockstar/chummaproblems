# Given a array with n elements print the number of
# occurrences of that number each number in that array.
# The order of number doesn't matter. You can reorder
# the elements.
# Input
# Array: [2,1,3,2,2,5,8,9,8]
# Output
# 2-3
# 1-1
# 3-1
# 5-1
# 8-2
# 9-1

a=list(map(int,input().split()))
b=list(set(a))
for i in b:
    print(i,a.count(i))