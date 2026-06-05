number=[78,45,92,35,88,40,99,56]
for n in number:
    if n>40:
        print(n)


fail = 0
for n in number:
    if n<40:
        print("fail")
        fail+=1     
        print("total fail:",fail)

above_75 = []
for n in number:
    if n>75:
        above_75.append(n)
        print("above 75:",above_75)


