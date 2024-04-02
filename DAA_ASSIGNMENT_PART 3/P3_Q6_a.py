def two_sum_slow(arr, K):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == K:
                return True, (arr[i], arr[j])
    return False, None

# Example usage:
arr = [8, 4, 1, 6]
K = 10
found, pair = two_sum_slow(arr, K)
if found:
    print("Yes, there exists a pair that sums to", K, ":", pair)
else:
    print("No such pair exists.")
