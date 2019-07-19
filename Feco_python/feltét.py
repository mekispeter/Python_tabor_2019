import random

pizza = [
    ["Sonkás","sonka","sajt","paradicsom"],
    ["Pepperonis","pepperoni","sajt","paradicsom"],
    ["Szalámis","szalámi","paradicsom","sajt"],
    ["Ananászos","ananász","sajt","paradicsom","sonka"],
    ["Mozarelás","mozarela","paradicsom"],
    ["Mexikoi","paradicsom","sonka","kukorica"]]

nyeropizza = random.choice(pizza)

megvan = "nem"
hiba = 0
feltet = []
print ("Talád ki milyen pizzára gondoltam ? ")
while megvan != "igen" and hiba < 4:
    tipp = input(" ! Pizza neve vagy feltét?  ")
    if  tipp == nyeropizza[0]:
         print("Ügyes vagy eltalátad a pizzát")
         megvan = "igen"
    elif tipp in nyeropizza:
        print ("Igen van rajta")
        feltet.append(tipp)
        print ("Eddigi feltétek: ",feltet)
    else: 
        print("Nincs rajta ilyen feltét")
        hiba +=1


if hiba == 4:
     print ("Sorry vesztetél")
    
    

