def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    
    mid = len(arr) // 2
    left_half, left_count = merge_sort(arr[:mid])
    right_half, right_count = merge_sort(arr[mid:])
    
    sorted_arr, merge_count = merge(left_half, right_half)
    total_count = left_count + right_count + merge_count
    
    return sorted_arr, total_count

def merge(left, right):
    result = []
    count = 0
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            count += len(left) - i
            
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result, count

# Example usage:
A = [1, 13, 5, 2, 8, 7, 0]
sorted_A, inv_count = merge_sort(A)

print("The number of inversions that are possible are as follows:")
print("{", end=" ")
for i in range(len(sorted_A)):
    for j in range(i+1, len(sorted_A)):
        if A.index(sorted_A[i]) > A.index(sorted_A[j]):
            print("( {}, {} )".format(sorted_A[j], sorted_A[i]), end=" ")
print("}")
print("Total count of inversions are:", inv_count)
