import heapq

def merge_n_sorted_lists(lists):
  merged_list = []

  min_heap = []
  for i, lst in enumerate(lists):
    heapq.heappush(min_heap, (lst[0], i, 0))

  while min_heap:
    val, list_idx, element_idx = heapq.heappop(min_heap)
    merged_list.append(val)

    if element_idx + 1 < len(lists[list_idx]):
      heapq.heappush(min_heap, (lists[list_idx][element_idx + 1], list_idx, element_idx + 1))

  return merged_list

lists = [
  [10, 20, 30, 40],
  [15, 25, 35],
  [27, 29, 37, 48, 93],
  [32, 33]
]

merged_list = merge_n_sorted_lists(lists)
print(merged_list)
