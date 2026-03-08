


nums = [1,2,3,1,2,3,2]
val= 3
for i in nums:
    print(i)
    if i==val:
        nums.remove(3)


print(nums)