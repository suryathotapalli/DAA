def candies(n, arr):
    candies = [1] * n

    # Traverse from left to right
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            candies[i] = candies[i - 1] + 1

    # Traverse from right to left
    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    return sum(candies)

# Take user input for the number of elements
n = int(input("Enter the number of elements: "))

# Take user input for the array of integers
arr = []
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)

# Call the function with user input
result = candies(n, arr)

# Print the result
print("Minimum number of candies required:", result)
