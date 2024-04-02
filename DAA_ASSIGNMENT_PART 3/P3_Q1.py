def find_pair_with_sum(arr, target_sum):
    seen = set()

    for num in arr:
        complement = target_sum - num
        if complement in seen:
            return [complement, num]
        seen.add(num)

    return None

# Input unsorted integer array and target sum
arr = [8, 7, 2, 5, 3, 1]
target_sum = 10

result = find_pair_with_sum(arr, target_sum)
if result:
    print(f"Pair with sum {target_sum} found: {result}")
else:
    print("No pair found with the given sum.")
