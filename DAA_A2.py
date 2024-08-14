def mz(arr):
    # Base case: If the array has 1 or 0 elements, return it as is
    if len(arr) <= 1:
        return arr
    
    #Divide :
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    #Conquer :
    left_half = mz(left_half)
    right_half = mz(right_half)

    #Combining/Merging
    return merg(left_half, right_half)

def merg(left, right):
    result = []
    #Append non-zeros from left half
    for elem in left:
        if elem != 0:
            result.append(elem)
    #Append non-zeros from right half
    for elem in right:
        if elem != 0:
            result.append(elem)
    #count the no of zeros and append them
    zeros_count = left.count(0) + right.count(0)
    result.extend([0] * zeros_count)
    return result

if __name__ == "__main__":
    size = int(input("Enter array size: "))
    arr = []
    print("Enter array elements: ")
    for i in range(size):
        arr.append(int(input()))
    result = mz(arr)
    print("Array is:", end=" ")
    for i in range(size):
        print(result[i], end=" ")
