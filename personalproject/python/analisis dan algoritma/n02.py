import time
import matplotlib.pyplot as plt

def A(n):
    start_time = time.time()
    total_iterations = 0  # To keep track of total iterations for comparison
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            total_iterations += 1
            print('x', end='')  # To avoid a large amount of output
    end_time = time.time()
    duration = end_time - start_time
    return duration, total_iterations

n_values = [10, 10**2, 10**3]
durations = []
iterations = []

for n in n_values:
    duration, total_iterations = A(n)
    durations.append(duration)
    iterations.append(total_iterations)
    print(f"n = {n}: Duration = {duration:.6f} seconds")

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(n_values, durations, marker='o')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('n values')
plt.ylabel('seconds')
plt.title('Durations for Different n values')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(n_values, iterations, marker='o')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('n')
plt.ylabel('Total Iterations')
plt.title('Comparison of Total Iterations for Different n')
plt.grid(True)

plt.tight_layout()
plt.show()
