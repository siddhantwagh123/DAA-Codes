#Implement a problem of smallest no with atleast n trailing zeroes in factorial.

def trailing_zeroes(n):
    #Initialize count
    count = 0
    #Start with 5 (since 5 is the factor responsible for trailing zeroes in factorials)
    i = 5
    #Loop to count how many times n can be divided by powers of 5
    while n // i >= 1:
        count += n//i
        i*=5
    return count

def smallest_no(n):
    #Initialize binary search range
    low, high = 0, 5*n 
    while low < high:
        #Calculate the midpoint of the current range
        mid=(low+high)//2
        
        #Check the number of trailing zeroes in mid!
        if trailing_zeroes(mid)>=n:
            #If mid has enough trailing zeroes,narrow search to the left half
            high = mid
        else:
            #Otherwise, search in the right half
            low = mid+1
    #When the loop ends, low == high, which is the smallest number with at least n trailing zeroes
    return low

n = int(input("Enter the number of trailing zeroes: "))
print("Smallest number whose factorial contains at least",n,"trailing zeroes is:", smallest_no(n))

