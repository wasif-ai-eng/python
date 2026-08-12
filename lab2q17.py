n=int(input("Enter a number:"))
seven=0
sodd=0
for i in range(1,n+1):
    if i%2==0:
        seven+=1
    else:
        sodd+=1


print("Sum even:",seven)
print("Sum odd:",sodd)