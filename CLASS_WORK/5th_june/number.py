number=[]

for i in range(20):
    n = int(input("enter a number:"))
    number.append(n)

result = [] #stores only unique numbers
for n in number:
    if n not in result:
        result.append(n)

        print("result:",result)
