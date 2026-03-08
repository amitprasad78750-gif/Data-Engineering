
import array


my_array1=array.array('i',[1,2,3,4,5,6])

def liner_searchs(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print(liner_searchs(my_array1,5))