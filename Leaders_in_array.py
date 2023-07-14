def find_leaders(A):
    result = []
    max_value = float('-inf')
    for i in range(len(A)-1, -1, -1):
        if A[i] > max_value:
            result.append(A[i])
            max_value = A[i]
    result.reverse()
    return result
A=list(map(int,input().split()))
print(find_leaders(A))

 