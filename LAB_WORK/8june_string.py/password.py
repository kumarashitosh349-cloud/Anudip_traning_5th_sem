pwd = "Python@2026!"

u = sum(1 for i in pwd if i.isupper())
l = sum(1 for i in pwd if i.islower())
d = sum(1 for i in pwd if i.isdigit())

s =  sum(1 for i in pwd if not i.isalnum())

digits = [i for i in pwd if i.isdigit()]
special =  [i for i in pwd if not i.isalnum()]

if len(pwd) >= 8 and u >= 1 and l >= 1 and d >= 1 and s >= 1:
    strength = "Strong"
elif len(pwd) >= 8:
     strength = "Medium"
else:
     strength = "Weak"


print("Uppercase:", u)

print("Lowercase:", l)

print("Digits:", d)

print("Special:", s)

print("Digits List:", digits)

print("Special List:", special)

print("Password Strength:", strength)