
nums=[1,2,3,4,1,2,2,3,2]
updateNums=[]
k=0
for i in range(len(nums)):
    x=nums[i]
    print(x)
    for j in nums:
        if j !=x:
            updateNums[k]=x
            k +=1
print(updateNums)