import numpy as np

v1 = np.array(list(map(int, input("Enter vector 1: ").split())))
v2 = np.array(list(map(int, input("Enter vector 2: ").split())))

print("Vector 1:", v1)
print("Vector 2:", v2)
print("Addition:", v1 + v2)
print("Subtraction:", v1 - v2)
print("Dot Product:", np.dot(v1, v2))
