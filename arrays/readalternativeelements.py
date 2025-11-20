arr = [1,2,3,4,5,6,7,8,9,10]
print(arr)
for index in range(0,len(arr),2):
    print(arr[index],end=", ")




def alternativeelements(arr):
    result = []
    for index in range(0,len(arr),2):
        result.append(arr[index])
    return result
print()
print(alternativeelements(arr))
