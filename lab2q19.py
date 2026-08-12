n = int(input("Enter a number: "))

for i in range(1, n + 1):

    if i == 3:
        pass
        print("Pass:", i)

    if i == 5:
        continue

    if i == 8:
        break

    print("Number:", i)