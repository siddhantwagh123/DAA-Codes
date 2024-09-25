'''Implement Subset Sum Problem.
Statement Given a set of non-negative integers and a
value sum, the task is to check if there is a subset of the
given set whose sum is equal to the given sum.
Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output: True
Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 30
Output: False'''

def subset(arr, n, sum_val):
    # Initialize a flag to check if subset sum exists
    flag = False

    # Check each possible pair of elements in the array
    for i in range(n):
        for j in range(i, n):
            if arr[i] + arr[j] == sum_val:
                flag = True
                break  # Exit loop early if subset is found

    # Output the result based on flag value
    if not flag:
        print("False")
    else:
        print("True")


# Main function to take input and call subset function
if __name__ == "__main__":
    n = int(input("Enter array size: "))
    arr = []

    print("Enter array elements: ")
    for i in range(n):
        arr.append(int(input()))

    sum_val = int(input("Enter sum: "))
    
    subset(arr, n, sum_val)
