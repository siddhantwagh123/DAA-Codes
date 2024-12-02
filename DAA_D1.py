'''Implement program to find all distinct subsets of a
given set using Bit Masking Approach.
Statement Given an array of integers arr[], The task is
to find all its subsets. The subset cannot contain
CO4
Sanjivani College of Engineering, Kopargaon Page 40 of 100
duplicate elements, so any repeated subset should be
considered only once in the output.
Input: S = {1, 2, 2} Output: {}, {1}, {2}, {1, 2}, {2,
2}, {1, 2,2}
Input: S = {1, 2} Output: {}, {1}, {2}, {1, 2}'''

def find_distinct_subsets(arr):
    # Ensure input is sorted to handle duplicates
    arr.sort()
    unique_subsets = set()
    
    # Generate all subsets using bit masking
    n = len(arr)
    for mask in range(1 << n):  # Iterate from 0 to 2^n
        subset = []
        for i in range(n):
            if mask & (1 << i):  # Check if the i-th element is included in the subset
                subset.append(arr[i])
        unique_subsets.add(tuple(subset))  # Use tuple to make it hashable for set
    
    # Print all unique subsets
    print("{", end="")
    for subset in unique_subsets:
        print("{", end="")
        print(", ".join(map(str, subset)), end="")
        print("}", end=", ")
    print("}")

if __name__ == "__main__":
    # Input the array
    arr = []
    n = int(input("Enter size of array: "))
    print("Enter array elements: ")
    for _ in range(n):
        arr.append(int(input()))
    
    # Call the function
    find_distinct_subsets(arr)
