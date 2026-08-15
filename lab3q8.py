# Create a tuple
t1 = (10, 20, 30, 40, 50)

print("Original tuple:", t1)

# Indexing
print("Element at index 0:", t1[0])
print("Element at index 2:", t1[2])

# Slicing
print("Elements from index 1 to 3:", t1[1:4])
print("First three elements:", t1[:3])
print("Last two elements:", t1[-2:])

# Create another tuple
t2 = (60, 70, 80)

# Concatenation
t3 = t1 + t2

print("Second tuple:", t2)
print("After concatenation:", t3)