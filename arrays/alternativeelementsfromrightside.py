arr = [1,2,3,4,5,6,7,8,9,10]
print(arr)
for i in range(len(arr)-1,-1,-2):
    print(arr[i])


arr = [1,2,3,4,5,6,7,8,9,10,12,334]
print(arr)
def readalternative(arr):
    result = []
    for i in range(len(arr)-1,-1,-2):
        result.append(arr[i])
    return result

print(readalternative(arr))
