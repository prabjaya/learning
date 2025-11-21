def twosum(nums,target):
    ans = [0] * 2
    map = {}

    for i in range(len(nums)):
        compliment = target - nums[i]
        if compliment in map:
            ans[0] = map[compliment]
            ans[1] = i
            return ans
        map[nums[i]] = i
    return None


nums = [0,2,3,4,5,6,7,8,9,10]
target =6

result = twosum(nums,target)
print(result)