n = int(input("Enter number of elements in the list: "))
arr = []

for i in range(n):
    arr.append(int(input("Enter element: ")))

new_arr = []

for i in range(n):
    if arr[i] not in new_arr:
        new_arr.append(arr[i])

print("List after removing duplicates:", new_arr)