arr = [1,2,3,4,5,6,7,8,9,10]

print(arr)
rightshiftbyone = arr[-1:] + arr[:-1]
print("Rightshiftbyone")
print(rightshiftbyone)


print("Rightshiftbytwo")

rightshiftbytwo = arr[-2:] + arr[:-2]
print(rightshiftbytwo)