'''Implement program to print all subsets of a given
Set or Array
Statement Given a set of positive integers, find all its
subsets.
Input: array = {1, 2, 3}
Output: // this space denotes null element.
1 1 2 1 2 3 1 3 2
2 3 3
Input: 1 2
Output: 1 2 1 2'''

def print_all_subsets(arr):
    # Sort the array (optional if no duplicates or specific order isn't needed)
    arr.sort()
    subsets = set()
    n = len(arr)

    # Generate all subsets using bit masking
    for mask in range(1, 1 << n):  # Start from 1 to exclude the empty subset
        subset = []
        for i in range(n):
            if mask & (1 << i):  # Check if the i-th bit is set
                subset.append(arr[i])
        subsets.add(tuple(subset))  # Convert list to tuple to use it in a set

    # Print all unique subsets
    for subset in subsets:
        print("       ", end="")
        print(" ".join(map(str, subset)), end="       ")
    print()

if __name__ == "__main__":
    # Input the array
    arr = []
    n = int(input("Enter size of array: "))
    print("Enter array elements: ")
    for _ in range(n):
        arr.append(int(input()))

    # Call the function
    print_all_subsets(arr)
