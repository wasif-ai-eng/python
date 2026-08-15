n1 = int(input("Enter number of elements in the first list: "))
l1 = []

for i in range(n1):
    l1.append(int(input("Enter element: ")))

n2 = int(input("Enter number of elements in the second list: "))
l2 = []

for i in range(n2):
    l2.append(int(input("Enter element: ")))

n3 = n1 + n2
l3 = []

for i in range(n1):
    l3.append(l1[i])

for i in range(n1, n3):
    l3.append(l2[i - n1])

for i in range(n3):
    print(l3[i], end=" ")