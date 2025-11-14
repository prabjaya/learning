arr = [12,34,45,67,65,90,13]

print(arr)
found = False
for element in reversed(arr):
    if element %2!== 0:
        found = True