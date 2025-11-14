def linersearch(arr,key):
    index = -1
    for i in range(len(arr)):
        if arr[i] == key:
            index = i
            break
    return index
        
arr = [1,2,4,3,5,7,6,8]

print(linersearch(arr,5))

print(linersearch(arr,10))