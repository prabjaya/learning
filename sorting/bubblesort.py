def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    

arr = [10,2,5,4,0,34,56,23,12,35]
print(arr)

bubblesort(arr)
print(arr)