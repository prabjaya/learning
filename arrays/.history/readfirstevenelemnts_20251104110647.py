arr =[1,3,5,7,17,19,23]
found  = False
print(arr)
for element in arr:
    if element % 2 == 0:
        print("First even element is ",element)
        found  = True
        break
if not found:
    print("No even elemnts ")



foundindex = False
print(arr)

for i in range(len(arr)):
    