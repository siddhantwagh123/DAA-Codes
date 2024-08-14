#Counting the no of zero's in an array
def count_zeros(arr):
    low, high=0, len(arr)-1
    while low<=high:
        #Divide step
        mid=low + (high - low) // 2
        #Conquer step
        if arr[mid]==0:
            #Check if this is the first occurence of zero
            if mid==0 or arr[mid-1]==1:
                #combine step
                return len(arr)-mid
            else:
                #Focus on the left half
                high=mid-1
        else:
            #Focus in the right half
            low=mid+1
            
    return 0

arr=[1, 1, 1, 1, 0, 0]
# a=list(input("enter the array : "))
print(count_zeros(arr))  
