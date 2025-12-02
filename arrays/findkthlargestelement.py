def solutionfind(n,arr,k):
    total = len(arr)
    for i in range(total):
      for j in range(total-1-i):
         if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr[-k]

n=5
arr=[10,20,30,40,50]
k=2

result = solutionfind(n,arr,k)
print(result)