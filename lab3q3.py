n=[]
sum=0
k=int(input("Enter the number of elements: "))
for i in range(k):
    a=int(input("Enter a number: "))
    n.append(a)
    sum=sum+a

print("Sum:",sum)
print("Average:",(sum/k))