#include <stdio.h>
// Java program for implementation of Insertion Sort 
void InsertionSort(int* arr ,int n){
    int temp;     // tempvarible for holding the element as sorting element
    for (int  i = 1; i < n; i++)
    {   int j = i-1;
     	temp=arr[j+1]; // the key  stored here 
     /* Move elements of arr[0..i-1], that are  greater than key, to one position ahead of their current position */
        while ((j>=0) && arr[j]>arr[j+1])  //condition for check the swpe nnededor the o the elements comes or not 
        {
            
            arr[j+1]=arr[j];
            j--;
        }
        arr[j+1]=temp;
        
    }
    
     
}
void printArray(int arr[], int size) 
{ 
	int i; 
	for (i=0; i < size; i++) 
		printf("%d ", arr[i]); 
	printf("\n"); 
}

int main() 
{   int size;
    printf("Enter the number of element in the array:");
    scanf("%d",&size);
	int arr[size]; 
    printf("Enter the array elements: \n");
    for(int i=0;i<size;i++){
        scanf("%d",&arr[i]);
    }
	int n = sizeof(arr)/sizeof(arr[0]); 
	InsertionSort(arr, n); 
	printf("Sorted array: \n"); 
	printArray(arr, n); 
	return 0; 

}  
