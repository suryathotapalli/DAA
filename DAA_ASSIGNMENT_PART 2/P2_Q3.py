import heapq

def find_k_largest(arr, k):
    if k >= len(arr):
        return sorted(arr, reverse=True)
    
    # Initialize a min-heap with the first K elements
    heap = arr[:k]
    heapq.heapify(heap)
    
    # Iterate through the remaining elements
    for num in arr[k:]:
        if num > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, num)
    
    # Return the K largest elements from the heap
    return sorted(heap, reverse=True)

# Example usage:
arr = [3, 10, 4, 7, 8, 20]
k = 3
result = find_k_largest(arr, k)
print("The", k, "largest elements in the array are:", result)
