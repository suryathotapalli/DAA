import time
import random
import matplotlib.pyplot as plt

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [random.randint(1, 1000) for _ in range(10000)]

search_keys = [int(input("Enter search key {} : ".format(i + 1))) for i in range(5)]

linear_times = []
for key in search_keys:
    start_time = time.time()
    linear_search(arr, key)
    end_time = time.time()
    linear_times.append(end_time - start_time)

binary_times = []
for key in search_keys:
    start_time = time.time()
    arr.sort() 
    binary_search(arr, key)
    end_time = time.time()
    binary_times.append(end_time - start_time)

plt.figure(figsize=(10, 6))
plt.plot(range(1, 6), linear_times, label='Linear Search')
plt.plot(range(1, 6), binary_times, label='Binary Search')
plt.xlabel('Search')
plt.ylabel('Time Taken (seconds)')
plt.title('Time Taken for Linear and Binary Search')
plt.xticks(range(1, 6), labels=['Search 1', 'Search 2', 'Search 3', 'Search 4', 'Search 5'])
plt.legend()
plt.grid(True)
plt.show()
