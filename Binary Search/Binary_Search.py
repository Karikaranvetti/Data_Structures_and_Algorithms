import array as Arr
import math
def Binary_Search(arr,data):
    left=0    #left pointer
    right=len(arr)  #right pointer 
    while right>left:    #whole array checkup
        mid=math.floor( (left+right)/2)
        if mid==data:
            return mid
        elif arr[mid]<data:
            left=mid+1
        else:
            right=mid-1
    return -1

if __name__ == "__main__":
    arr=Arr.array=[1,2,3,4,5,6,7,8,9,10]   # for binary search array should be sored 
    try:
        key=int(input('Enter the key for search :'))
    except Exception     as identifier:
         
        raise identifier
    
    m=Binary_Search(arr,key)
    if m>-1:
        print('the {} is in {} place '.format(key,m))
    else:
        print('the {} is not in the array'.format(key))
        
            