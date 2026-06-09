plate = "MH12AB4589"

state = plate[0:2]
district = plate[2:4]
series = plate[4:6]

number =  plate[6:]

letters = 0
digits = 0

for i in plate:
    if i.isalpha():
        letters += 1
    elif i.isdigit():
        digits += 1

valid  = (plate[0:2].isalpha() and
     plate[2:4].isdigit() and
         plate[4:6].isalpha() and
         plate[6:].isdigit())

print("State:", state)
print("District:" , district)
print("Series:", series)
print("Number:", number)
print("Letters:", letters)
print("Digits:", digits)

if valid:
    print("VALID")
else:
    print("INVALID")
