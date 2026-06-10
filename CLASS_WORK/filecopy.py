a = open("data.txt", "r")
data = a.read()
a.close()

b = open("copy.txt", "w")

b.write(data)
b.close()

print("Copied successfully")