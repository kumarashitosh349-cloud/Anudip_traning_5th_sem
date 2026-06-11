cart = [1500, 899, 450, 2500, 799, 1200, 300, 650, 1800, 999]
 
 #total cart value
total=0
sum=0
for i in cart:
    total+=i
    print(total)

#most expensive and cheapest
most_expensive=0
most_cheap=0
for i in cart:
    if(i>most_expensive):
        most_expensive==i
        print("mostexpensive",i)
        
    elif i<most-cheap :
        most_cheap==j
        print("most_cheap",i)

#premium_shipping
count=0
for i in cart:
    if(i>1000):
     count+=1
     print("premiun product",count)

#average
     avg=total/len(cart)
     print("avg:",avg)

        




        
        
