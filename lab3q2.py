num=[1,2,3,4,5,6,7,8,9]
max=num[0]
min=num[0]
for i in num:
    if i>max:
        max=i
    if i<min:
        min=i

print("Max:",max)
print("Min:",min)    