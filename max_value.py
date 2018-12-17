i=int(input("Enter integer number:"))
a = -1
while i > 0:
    b = i % 10
    i = i//10
    if b > a:
        a = b
print("Max value=",a)