present=0
absent=0
n=int(input("enter total number of students"))
for i in range(n):
    s=input("p for present or a for absent")
    if s=="p":
        present+=1
    elif s=="a":
        absent+=1

print("total present:", present)
print("total absent:", absent)

 ## python_u "CLASS_WORK\areaoftriangle.py"
