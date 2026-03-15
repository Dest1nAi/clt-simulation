import numpy as np
import matplotlib.pyplot as plt

n = 30
N = 10000

means = []

for i in range(N):
    sample = np.random.exponential(scale=1, size=n)
    means.append(np.mean(sample))

plt.hist(means, bins=50, density=True)
plt.title("Central Limit Theorem Simulation")
plt.xlabel("Sample mean")
plt.ylabel("Density")
plt.savefig("clt_histogram.png")
plt.show()