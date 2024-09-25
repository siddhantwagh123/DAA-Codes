'''Implement Coin Change problem.
Statement Given an integer array of coins[ ] of
size N representing different types of currency and an
integer sum, The task is to find the number of ways to
make sum by using different combinations
from coins[].
Note: Assume that you have an infinite supply of each
type of coin.
Input: sum = 4, coins[] = {1,2,3}, Output: 4
Input: sum = 10, coins[] = {2, 5, 3, 6} Output: 5'''

def count_ways(sum_val, n, coins):
    # Initialize a list to store the number of ways to make each sum
    count = [0] * (sum_val + 1)
    count[0] = 1  # Base case: There's 1 way to make sum 0 (by choosing no coins)

    # Iterate over each coin
    for i in range(n):
        # Update count array for sums >= coins[i]
        for j in range(coins[i], sum_val + 1):
            count[j] += count[j - coins[i]]

    # Output the number of ways to make the given sum
    print(f"Ways to make sum {sum_val}: {count[sum_val]}")


# Main function to take inputs and call count_ways function
if __name__ == "__main__":
    sum_val = int(input("Enter value of sum: "))
    n = int(input("Enter total number of coins: "))
    
    coins = []
    print("Enter coins: ")
    for i in range(n):
        coin = int(input())
        coins.append(coin)
    
    count_ways(sum_val, n, coins)
