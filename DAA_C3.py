'''Implement Check if it is possible to transform one
string to another.
Statement Given two strings s1 and s2 (all letters in uppercase).
Check if it is possible to convert s1 to s2 by performing following
operations.
1. Make some lowercase letters uppercase.
2. Delete all the lowercase letters.
Input: s1 = daBcd s2 = ABC Output: yes
Input: s1 = argaju s2 = RAJ Output: yes'''

def check(s1, s2):
    # Convert both strings to lowercase
    a = s1.lower()
    b = s2.lower()
    
    i,j = 0,0
    # Iterate through both strings
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            j += 1  # Move to the next character in s2 if we find a match
        i += 1  # Always move to the next character in s1
    
    # If we've matched all characters of s2, it's possible to transform
    if j == len(b):
        return "YES"
    else:
        return "NO"

# Input
s1 = input("Enter string 1: ")
s2 = input("Enter string 2: ")

# Output the result
print(check(s1, s2))
