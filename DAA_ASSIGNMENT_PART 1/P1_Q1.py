import time
import matplotlib.pyplot as plt

# Iterative algorithm to find sum of first N natural numbers
def iterative_sum(N):
    total = 0
    for i in range(1, N + 1):
        total += i
    return total

# Recursive algorithm to find sum of first N natural numbers
def recursive_sum(N):
    if N == 0:
        return 0
    return N + recursive_sum(N - 1)

# Function to measure execution time
def measure_time(func, N):
    start_time = time.time() * 1000  # Convert to milliseconds
    func(N)
    end_time = time.time() * 1000  # Convert to milliseconds
    return end_time - start_time

# Varying values of N
N_values = list(range(1, 1001, 50))

# Measure time taken by iterative algorithm for each N
iterative_times = [measure_time(iterative_sum, N) for N in N_values]

# Measure time taken by recursive algorithm for each N
recursive_times = [measure_time(recursive_sum, N) for N in N_values]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(N_values, iterative_times, label='Iterative')
plt.plot(N_values, recursive_times, label='Recursive')
plt.xlabel('Value of N')
plt.ylabel('Time (milliseconds)')
plt.title('Time taken to compute sum of first N natural numbers')
plt.legend()
plt.grid(True)
plt.show()
