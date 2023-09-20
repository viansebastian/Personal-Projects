import time
import matplotlib.pyplot as plt

def A(n):
    start_time = time.time()
    i = 1
    while i <= n:
        print('x', end='')  # To avoid a large amount of output
        i = i * 2
    end_time = time.time()
    duration = end_time - start_time
    return duration

n_values = [10**100, 10**120, 10**150, 10**200, 10**250]
durations = []

for n in n_values:
    duration = A(n)
    durations.append(duration)
    print(f"n = {n}: Duration = {duration:.6f} seconds")

plt.plot(n_values, durations, marker='o')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('n')
plt.ylabel('Duration (seconds)')
plt.title('Comparison of Durations for Different n')
plt.grid(True)
plt.show()
