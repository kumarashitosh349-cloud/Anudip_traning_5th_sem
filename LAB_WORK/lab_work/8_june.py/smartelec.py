
units = {
    "House101": 320,
    "House102": 180,
    "House103": 510,
    "House104": 275,
    "House105": 150,
    "House106": 430,
    "House107": 220,
    "House108": 390,
    "House109": 145,
    "House110": 600
}

more_400=[]
low=[]
meduim=[]
high=[]

totl=0
count=0

max_u=0
min_u=9999
higest_house=""
lowst_house=""

for h in units:
    u=units[h]

    totl=totl+u

    if u>400:
        more_400.append(h)

    if u<200:
        low.append(h)
    elif u<=400:
        meduim.append(h)
    else:
        high.append(h)

    if u>300:
        count=count+1

    if u>max_u:
        max_u=u
        higest_house=h

    if u<min_u:
        min_u=u
        lowst_house=h

print("More then 400 houses are:", more_400)
print("Higest consuming house:", higest_house)
print("Lowst consuming house:", lowst_house)
print("Totl units:", totl)
print("Low cons:", low)
print("Meduim cons:", meduim)
print("High cons:", high)
print("Count houses >300:", count)
