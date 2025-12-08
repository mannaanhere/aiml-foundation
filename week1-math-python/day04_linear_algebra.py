import numpy as np
from sklearn.model_selection import train_test_split


# 1. Create a simple dataset ------------------------------------

# Each row = [Hours studied, Sleep hours, Marks]
data = np.array([
    [2, 6, 40],
    [4, 7, 50],
    [6, 8, 60],
    [8, 7, 70],
    [10, 9, 90]
], dtype=float)

print("Original Dataset:\n", data)
print("-" * 50)


# 2. Introduce & handle missing values --------------------------

# Add a missing value artificially
data[2, 1] = np.nan   # Sleep hours missing

print("Dataset with Missing Value:\n", data)

# Replace missing values with column mean
col_mean = np.nanmean(data, axis=0)
inds = np.where(np.isnan(data))
data[inds] = np.take(col_mean, inds[1])

print("After Handling Missing Values:\n", data)
print("-" * 50)


# 3. Feature & target separation --------------------------------

X = data[:, :-1]   # input features (hours, sleep)
y = data[:, -1]    # output (marks)

print("Features (X):\n", X)
print("Target (y):\n", y)
print("-" * 50)


# 4. Feature scaling (Standardization from scratch) -------------

mean = X.mean(axis=0)
std = X.std(axis=0)
X_scaled = (X - mean) / std

print("Scaled Features (X_scaled):\n", X_scaled)
print("Mean:", mean)
print("Std:", std)
print("-" * 50)


# 5. Train-Test split -------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

print("Training Features:\n", X_train)
print("Testing Features:\n", X_test)
print("Training Target:", y_train)
print("Testing Target:", y_test)
print("-" * 50)


