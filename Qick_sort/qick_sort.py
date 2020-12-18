def parttion(arr,start,end):
    mid=start-1  #partion mid point
    pivote=arr[end]  # the pivote value is last element 

    for i in range(start,end):    # we checking all elements expect last value 
        if arr[i]<=pivote: # the checking element less than pivote then put into mid index 
            mid=mid+1
            arr[mid],arr[i]=arr[i],arr[mid]    # exchange the value 
        
    arr[mid+1],arr[end]=arr[end],arr[mid+1]   # finaly put into correct place to pivote 
    return mid+1

def qickSort(arr,start,end):
    if start<end:
        mid=parttion(arr,start,end)
        qickSort(arr,start,mid-1)   # recursive call 
        qickSort(arr,mid+1,end)


if __name__ == "__main__":   #sample test 
    arr = [64, 34, 25, 12, 22, 11, 90] 

    qickSort(arr,0,6) 

    print ("Sorted array :") 
    for i in range(len(arr)): 
	    print ("%d" %arr[i],end=" ") 
    print('')