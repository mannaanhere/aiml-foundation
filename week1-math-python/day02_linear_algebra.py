# Vector Addition and Multiplication

def add_vectors(v1, v2):
    return [v1[i] + v2[i] for i in range(len(v1))]

def multiply_vectors(v1, v2):
    return [v1[i] * v2[i] for i in range(len(v1))]

# Example Vectors
v1 = [1, 2, 3]
v2 = [4, 5, 6]

sum_vector = add_vectors(v1, v2)
product_vector = multiply_vectors(v1, v2)

print("Vector 1:", v1)
print("Vector 2:", v2)
print("Addition:", sum_vector)
print("Multiplication:", product_vector)
