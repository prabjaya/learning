arr = [1,2,3,4,5,6,7,8,9,10]
index = -1
key = 5

for i in range(len(arr)):
    if arr[i] == key:
        index = 1
        break
print(f"{key} is available" if index != -1 else f"{key} is not available")

