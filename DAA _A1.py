#Counting the no of zero's in an array
def count_zeros(arr):
    low, high=0, len(arr)-1
    while low<=high:
        mid=low + (high - low) // 2
        
        if arr[mid]==0:
            
            if mid==0 or arr[mid-1]==1:
                return len(arr)-mid
            else:
                high=mid-1
        else:
            low=mid+1
            
    return 0

arr=[1, 1, 1, 1, 0, 0]
# a=list(input("enter the array : "))
print(count_zeros(arr))  
