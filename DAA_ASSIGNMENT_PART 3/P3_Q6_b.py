def two_sum_fast(arr, K):
    arr.sort()  # Sort the array
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == K:
            return True, (arr[left], arr[right])
        elif current_sum < K:
            left += 1
        else:
            right -= 1
    return False, None

# Example usage:
arr = [8, 4, 1, 6]
K = 10
found, pair = two_sum_fast(arr, K)
if found:
    print("Yes, there exists a pair that sums to", K, ":", pair)
else:
    print("No such pair exists.")
