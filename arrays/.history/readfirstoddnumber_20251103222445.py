arr = [24,45,5,67,78,90,13]

print(arr)

for element in arr:
    if element %2 != 0 :
        print("The first odd element is ",element)
        found = True
        break
if not found:
    print("The ")