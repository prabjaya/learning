arr = [13,15,17,19,30,89,33,35,39]
print(arr)
count = 0
found =False
for element in arr:
    if element %2 != 0:
        count +=1
        if count == 3:
            print("The third odd element is", element)
            found = True
            break
if not found:
    print("No odd elements in the given array")

