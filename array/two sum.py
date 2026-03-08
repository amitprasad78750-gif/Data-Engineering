
# find pairs
arry_nums = [9,4,10,5,7,8,6]
def findPairs(arry_nums,target):
    for i in range(len(arry_nums)):
        for j in range(i+1,len(arry_nums)):
            if arry_nums[i] + arry_nums[j] == target:
                print(i,j)

findPairs(arry_nums,15)