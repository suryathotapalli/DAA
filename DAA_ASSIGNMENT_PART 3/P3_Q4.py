def segregate_0_1(arr):
  
  left_idx = 0
  right_idx = len(arr) - 1

  while left_idx < right_idx:
    while left_idx < right_idx and arr[left_idx] == 0:
      left_idx += 1

    while left_idx < right_idx and arr[right_idx] == 1:
      right_idx -= 1

    if left_idx < right_idx:
      arr[left_idx], arr[right_idx] = arr[right_idx], arr[left_idx]

arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
segregate_0_1(arr)
print(arr)
