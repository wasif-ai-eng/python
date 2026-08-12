n=int(input("Enter a number:"))
reverse=0
original=n
while n!=0:
    reverse=reverse*10+n%10
    n=n//10

if(reverse==original):
        print("palindrome")
else:
        print("not a palindrome")