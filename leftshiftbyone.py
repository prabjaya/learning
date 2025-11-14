arr = [1,2,3,4,5,6,7,8,9,10]


print("Original Array")
print(arr)

print("leftshiftbyone")
leftshiftbyone = arr[1:] + arr[:1]
print(leftshiftbyone)

print("leftshiftbytwo")
leftshiftbytwo = arr[2:] + arr[:2]
print(leftshiftbytwo)