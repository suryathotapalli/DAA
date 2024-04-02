def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])  # Sort intervals based on the start time
    merged = [list(intervals[0])]

    for current_start, current_end in intervals:
        previous_start, previous_end = merged[-1]
        if current_start <= previous_end:  # Check for overlapping intervals
            merged[-1] = [previous_start, max(previous_end, current_end)]
        else:
            merged.append([current_start, current_end])

    return merged

# Input intervals as pairs of start and end times
intervals = [(1, 4), (2, 5), (7, 8), (6, 9)]

result = merge_intervals(intervals)
print("Non-overlapping intervals after merging:")
print(result)
