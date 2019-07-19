import random

jelszolista = ["Feco","Obi van kenobi","Luke Skywaker","Yoda"]
jelszo = random.choice(jelszolista)

talalgatas = input("jelszo: ")

if jelszo == talalgatas:    
   print("Dart Vader ki lojük a marsra")     
else:
    print("Sajna nem tudtal betorni :)")
