import random

jelszolista = ["Jelszó","123456789","Password"]

jelszo = random.choice(jelszolista) 

talalgatas = input("Jelszó:")

if jelszo == talalgatas:
    print("Történet+")
else:
    print("Történet-")

 
