import numpy as np
import statistics

np.random.seed(42)  
X = np.random.randint(1, 100, 10)  
Y = np.random.randint(1, 100, 10)

data = np.array([X, Y])

print("Data Set X:", X)
mean_x = np.mean(X)
median_x = np.median(X)
mode_x = statistics.mode(X)
std_dev_x = np.std(X)

print(f"Mean (X): {mean_x}")
print(f"Median (X): {median_x}")
print(f"Mode (X): {mode_x}")
print(f"Standard Deviation (X): {std_dev_x}")


print("Data Set Y:", Y)
mean_y = np.mean(Y)
median_y = np.median(Y)
mode_y = statistics.mode(Y)
std_dev_y = np.std(Y)

print(f"Mean (Y): {mean_y}")
print(f"Median (Y): {median_y}")
print(f"Mode (Y): {mode_y}")
print(f"Standard Deviation (Y): {std_dev_y}")
