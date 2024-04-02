def max_product_pair(arr):
    if len(arr) < 2:
        return None
    
    max1 = max(arr[0], arr[1])
    max2 = min(arr[0], arr[1])
    min1 = min(arr[0], arr[1])
    min2 = max(arr[0], arr[1])
    
    for i in range(2, len(arr)):
        if arr[i] > max1:
            max2 = max1
            max1 = arr[i]
        elif arr[i] > max2:
            max2 = arr[i]
        
        if arr[i] < min1:
            min2 = min1
            min1 = arr[i]
        elif arr[i] < min2:
            min2 = arr[i]
    
    return max(max1 * max2, min1 * min2)

arr = [1, 7, 4, 2, 8, 6, 3, 9, 5]
result = max_product_pair(arr)
print(result)
