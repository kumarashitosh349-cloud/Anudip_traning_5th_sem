num = input()

p = num.index(max(num))

print("Mountain Number" if all(num[i] < num[i+1] for i in range(p)) 
      and all(num[i] > num[i+1] for i in range(p, len(num)-1)) 
      else "Not a Mountain Number")