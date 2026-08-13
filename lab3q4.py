n=[]
k=int(input("Enter the number of elements: "))
for i in range(k):
    a=int(input("Enter a number: "))
    n.append(a)

key=int(input("Enter the number to search: "))
f=0
for i in n:
   if(i==key):
      f=1
if f==1:
 print("found")
else:
 print("not found")