## Also watch this: https://www.youtube.com/watch?v=W8oGaAEOeRU

# Prep stage:

# 1.create map with:
#   keys : values from input list,
#   values : indexes of values from input list,
# 2.make a copy of sorted input list

# Algo stage:
# 1.Iterate through input list, and compare current value (lets call it cv) against value from sorted list (lets call it scv). 
# If it is diffrent:
#  - increment number of swaps
#  - get index of the scv from map - map[scv],
#  - in input list swap cv with scv,
#  - update map[cv]=map[scv] (map[scv] does not need to be updated as we are not going to use it any more)
# 2.Then you need to execute it on input list and reversed input list - the smaller return value - is the answer.

# Time complexity is equal to sort time complexity (usually O(n logn) ). 
# Space O(n)

def solution(a):

    m = {}
    for i in range(len(a)):
        m[a[i]] = i 
        
    sorted_a = sorted(a)
    ret = 0
    
    for i in range(len(a)):
        if a[i] != sorted_a[i]:
            ret +=1
            
            ind_to_swap = m[ sorted_a[i] ]
            m[ a[i] ] = m[ sorted_a[i]]
            a[i],a[ind_to_swap] = sorted_a[i],a[i]
    return ret

input()
a = [int(i) for i in input().split(' ')]

asc=solution(list(a))
desc=solution(list(reversed(a)))
print(min(asc,desc))
