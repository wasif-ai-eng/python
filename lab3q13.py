n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    arr.append(int(input("Enter element: ")))
print("Original list:", arr)
unique = list(set(arr))
print("List after removing duplicates:", unique)
