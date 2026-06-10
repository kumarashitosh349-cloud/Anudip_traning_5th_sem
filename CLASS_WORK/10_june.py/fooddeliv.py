delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]

def fastest_delivery(times):
    fastest = times[0]

    for t in times:
        if t < fastest:
         fastest = t
    print("Fastest delivery time =", fastest)
    fastest_delivery(delivery_time)

def delayed_orders(times):
   delayed=[]
   for t in times:
      if t >45:
         delayed.append(t)
         return delayed
      
def average_delivery_time(times):
   total=0
   
   for t in times:
      total = total+t

     average = total/len(times)
   
     return average


          
