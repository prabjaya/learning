def binarysearch(arr,key):
    index = -1
    left = 0
    right = len(arr) - 1
    while(left <= right):
        mid = (left + right) // 2
        if arr[mid] == key:
            index = mid
            break
        elif arr[mid] < key:
            left = mid -1
        else:
            right = mid + 1
    return index

arr = [1,3,4,5,6,7,8]
print(binarysearch(arr,5))