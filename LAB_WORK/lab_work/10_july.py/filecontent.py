file =open ("first.txt","r")
content= file.read()
vowels= "aeiouAEIOU"


file_count=0
for ch in content:
    file.count+=1
    print("total vowels:",file_count)

chatractor_count=0
for ch in content:
    chatractor_count+=1 
print("total charactors:",chatractor_count)




file = open("first.txt", "r")


lines = file.readlines()


count = len(lines)


print("Total number of lines:", count)


file.close()



 

