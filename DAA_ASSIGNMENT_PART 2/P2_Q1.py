import random
import time
import matplotlib.pyplot as plt
import heapq

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Insertion Sort
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Bucket Sort
def bucket_sort(arr):
    # Determine the range of values in the array
    min_val = min(arr)
    max_val = max(arr)
    
    # Determine the range of each bucket
    bucket_range = (max_val - min_val) // 10 + 1

    # Create buckets
    buckets = [[] for _ in range(10)]

    # Distribute numbers into buckets
    for num in arr:
        index = (num - min_val) // bucket_range
        buckets[index].append(num)

    # Sort each bucket and update the original array
    k = 0
    for bucket in buckets:
        insertion_sort(bucket)
        for num in bucket:
            arr[k] = num
            k += 1

# Radix Sort
def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

def counting_sort(arr, exp):
    output = [0] * len(arr)
    count = [0] * 10

    for num in arr:
        index = num // exp % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = len(arr) - 1
    while i >= 0:
        index = arr[i] // exp % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(len(arr)):
        arr[i] = output[i]

# Heap Sort
def heap_sort(arr):
    heapq.heapify(arr)
    sorted_arr = []
    while arr:
        sorted_arr.append(heapq.heappop(arr))
    return sorted_arr

# Generate random numbers
random_numbers = [random.randint(1, 10000) for _ in range(1000)]

# Measure time taken by each sorting algorithm
sorting_algorithms = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort,
    "Bucket Sort": bucket_sort,
    "Radix Sort": radix_sort,
    "Heap Sort": heap_sort
}

sorting_times = {}
for algorithm_name, algorithm in sorting_algorithms.items():
    arr_copy = random_numbers.copy()
    start_time = time.time() * 1000  # Convert to milliseconds
    algorithm(arr_copy)
    end_time = time.time() * 1000  # Convert to milliseconds
    sorting_times[algorithm_name] = end_time - start_time

# Plotting
plt.figure(figsize=(12, 8))
plt.bar(sorting_times.keys(), sorting_times.values(), color='skyblue')
plt.xlabel('Sorting Algorithm')
plt.ylabel('Time (milliseconds)')
plt.title('Time taken by different sorting algorithms for 1000 random numbers')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
