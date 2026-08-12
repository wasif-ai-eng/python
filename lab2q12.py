n=int(input("Enter a number:"))
isprime=1
for i in range (2,n):
    if n%i==0:
        isprime=0
        break
if(isprime==1):
    print("prime")
else:
    print("not prime ")