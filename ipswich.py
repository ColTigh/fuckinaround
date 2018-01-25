#my first python script
#lets check for primes

x = int(input("number please: "))
 #print (x)
primebool = True
for num in range(2, x):
 if x%num == 0:
    primebool = False
if primebool:
  print ("PRIME!!!!")
else:
  print ("not prime, #sadface")
# lets see if it works
#cross our fingers
