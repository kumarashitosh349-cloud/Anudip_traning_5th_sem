parking_slots = [
"Occupied", "Vacant", "Occupied", "Vacant",
"Occupied", "Occupied", "Vacant", "Occupied",
"Vacant", "Occupied"]

#available seats
for i in parking_slots:
     if parking_slots[i] == "vacant":
          print(i+1)

#occupird and vacant
occupied=0
vacant=0
for i in parking_slots:
    if parking_slots[i]=="occupied":
          occupied+=1
    else:
          vacant+=1

#parking occupancy
occupency=occupied/len(parking_slots)
print("occupency:",occupency)


#first vacant slot
first_vacant=0
for i in parking_slots:
     if i>first_vacant:
          print("first_vacant:",i)

          

     
     
     

          
          
          


     