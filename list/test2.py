
nums1=[1,3]
nums2=[2]
new_lst=nums1+nums2
new_lst.sort()
list_length=len(new_lst)
mid = list_length//2

if list_length %2 ==1:
     median= new_lst[mid]
else:
    median=(new_lst[mid-1]+new_lst[mid])/2


print(median)