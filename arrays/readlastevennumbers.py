arr = [12,24,34,11,13,15,23,43]

print(arr)

found = False
for element in reversed(arr):
    if element %2 == 0:
        print("The last even element is", element)
        found = True
        break
if not found:
    print("No elements")        