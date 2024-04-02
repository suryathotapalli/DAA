def find_swapped_elements(arr):
    n = len(arr)
    first_swap = None
    second_swap = None

    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            if first_swap is None:
                first_swap = i
            else:
                second_swap = i + 1

    arr[first_swap], arr[second_swap] = arr[second_swap], arr[first_swap]
    return arr

# Input array with two swapped elements
arr = [3,8,6,7,5,9]

sorted_arr = find_swapped_elements(arr)
print("Sorted array after fixing the swapped elements:")
print(sorted_arr)
