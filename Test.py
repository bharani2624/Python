def min_cost_path(arr):
    n = len(arr)
    
    # Handle the case where the list has only one or two elements
    if n == 1:
        return arr[0]
    if n == 2:
        return min(arr[0], arr[1])

    # Initialize dp array
    dp = [0] * n
    dp[0] = arr[0]
    dp[1] = arr[1]
    
    # Fill the dp array for the rest of the indices
    for i in range(2, n):
        dp[i] = arr[i] + min(dp[i - 1], dp[i - 2])
    
    # The minimum cost to reach the end is the minimum of the last two dp values
    return min(dp[n - 1], dp[n - 2])

# Test cases
arr1 = [10, 15, 20]
arr2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]

print(min_cost_path(arr1))  # Output: 20
print(min_cost_path(arr2))  # Output: 6
