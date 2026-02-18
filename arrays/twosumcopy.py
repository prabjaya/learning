nums = [1,2,3,4,5,6,7,8,9]
target = 5


def twosum(nums,target):

    pair =[]

    for i in range(len(nums)):
        for j in range(i +1 , len(nums)):
            if nums[i]  + nums[j] == target:
                pair.append([i,j])
    return pair


print(twosum(nums,target))