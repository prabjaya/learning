arr = [1,2,3,4,5,6,7,8,9,10]
total = len(arr)

totalodd = 0
totaleven = 0
for element in arr:
    if element %2 == 0:
        totaleven +=1
    else:
        totalodd +=1

print("Toatal", total,"")