import random
import time


a1 = [random.randint(1, 99) for _ in range(20)]
a = a1.copy()

print("Initial array:")
print(a)


print("\nUsing Bubble sort:")
start_time = time.perf_counter_ns()
for i in range(len(a)):
    for j in range(len(a) - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
end_time = time.perf_counter_ns()
execution_time = end_time - start_time
print("Execution time:", execution_time, "nanoseconds")
print("Final array:")
print(a)


a = a1.copy()


print("\nUsing Insertion sort:")
start_time = time.perf_counter_ns()
for i in range(1, len(a)):
    key = a[i]
    j = i - 1
    while j >= 0 and key < a[j]:
        a[j + 1] = a[j]
        j -= 1
    a[j + 1] = key
end_time = time.perf_counter_ns()
execution_time = end_time - start_time
print("Execution time:", execution_time, "nanoseconds")
print("Final array:")
print(a)


a = a1.copy()


print("\nUsing Selection sort:")
start_time = time.perf_counter_ns()
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
end_time = time.perf_counter_ns()
execution_time = end_time - start_time
print("Execution time:", execution_time, "nanoseconds")
print("Final array:")
print(a)


a = a1.copy()


print("\nUsing Array sort:")
start_time = time.perf_counter_ns()
a.sort()
end_time = time.perf_counter_ns()
execution_time = end_time - start_time
print("Execution time:", execution_time, "nanoseconds")
print("Final array:")
print(a)
