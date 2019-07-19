pizza = [
    ["Sonkás",1995],
    ["Pepperonis",2905],
    ["Szalámis",1995],
    ["Ananászos",2395],
    ["Mozerela",2095]]


megvan = "nem"

while megvan != "igen":
    valasz = input("Milyen pizzat szeretnél? ")
    for sor in pizza:
        if sor[0] == valasz:
            print("Szuper ilyenük van ára: ",sor[1],"Forint")
            megvan = "igen"


