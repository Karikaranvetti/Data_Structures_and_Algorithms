''' this leaner sherch algorithem time complexcity for 
best case O(1)
waste case O(n)   '''


import array
def Lsearch(arr,key):
    
    for i in range(0,len(arr)):
        if arr[i]==key:
            return i
    return -1

if __name__ == "__main__":
   arr=array.array=[1,2,3,4,5,6,7,8,9,10]
   key=int(input('Enter the key for search :'))
   m=Lsearch(arr,key)
   if m>-1:
       print('the {} is in {} place '.format(key,m))
   else:
        print('the {} is not in the array'.format(key))