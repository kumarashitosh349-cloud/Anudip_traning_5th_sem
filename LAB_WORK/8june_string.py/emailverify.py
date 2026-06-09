email="rahul.sharma2026@gmail.com"
user = email[0:12]
print(user)

domain = email[17:22]
print(domain)

extention = email[16:17]

print(extention)

count=0
for i in email:
    if i.isdigit():
     count+=1

print("digits:", count)


   
   
   








