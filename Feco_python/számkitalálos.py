import random

print("Mondok egy számot 1 és 100 között. Taládki a számot")

veletlenszam = random.randrange(1,101)

valasz = 0
tippek = 0

while valasz != veletlenszam:
      valasz = int(input ("Mi a tiped?"))
      tippek += 1
      if valasz < veletlenszam:
          print ("Nem jo a válaszod   nagyob ra gondoltam")
      elif valasz > veletlenszam:
        print ("Nem jo kisebb re gondoltam ")
      elif valasz == veletlenszam:
        print ("Szuper el találtad")
        print ("Enyi szer tippeltél: ",tippek)
 
