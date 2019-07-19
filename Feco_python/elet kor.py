
ev = int (input("szuletesi eved :"))
valasz=input("emulte mar a szulinapod")
if valasz == "nem" or valasz == "igen":
     if valasz == "nem":
        evkor = 2018-ev
     if valasz == "igen":
       evkor = 2019-ev
     print("enyi eves vagy pontosan: ", evkor )
     evkor -=1
     print("2018ba enyi  eves voltal:", evkor )

else:
    print("Csak igen es nemmel lehet valaszolni")
    
