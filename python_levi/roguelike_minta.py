import sys
import pygame as pg
import random as r

def gyarts_szobakat_legyszi():
    # Kilenc szobát generálunk egy háromszor hármas négyzetben. Azt szeretnénk,
    # hogy középen mindenképpen legyen szoba, és ne legyenek elszigetelt szobák.
    # Először létrehozunk egy alaprajzot.
    # Az alaprajz fogja megadni a szobák mintázatát. Ez alapján hozzuk
    # majd létre a szobákat.
    # Az alaprajzról már leolvasható, hogy melyik szobának merre van
    # szomszédja. Ahol van szomszéd, oda fog folyosó vezetni. Ez fontos infó,
    # mert ennek alapján választunk majd a 45 szobakép közül.

    # Ezt a függvényt használjuk, ha el akarjuk dönteni, hogy valahol legyen-e
    # szoba. 2/3 valószínűséggel lesz. (False = nincs szoba, True = van szoba.)
    def szoba_sorsolas():
        return r.choice([False, True, True])

    #Akkor szomszédos egy szobahely egy másikkal, ha csak egy koordinátában térnek el, és abban is csak eggyel.
    szomszedok = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    # A szomszédok sorban: bal, felső, jobb, alsó. Ezt rövidítjük a B, F, J, L betűkkel a file-nevekben.
    szomszed_betuk = "BFJL"

    # Az alaprajzon először középre teszünk egy szobát, és körbe a szomszédaira
    # véletlenszerűen. A sarkokra még nem teszünk.
    alaprajz = [
        [False, szoba_sorsolas(), False],
        [szoba_sorsolas(), True, szoba_sorsolas()],
        [False, szoba_sorsolas(), False]]

    # A középső szoba nem maradhat egyedül. Ha a egyikére se került szoba, teszünk egyet felülre.
    if not max([alaprajz[1+szomszed[0]][1+szomszed[1]] for szomszed in szomszedok]):
        alaprajz[0][1] = True

    # A sarkokba akkor kerül szoba, ha a mellettük lévő oldalak valamelyikén
    # is van.
    if alaprajz[0][1] or alaprajz[1][0]:
        alaprajz[0][0] = szoba_sorsolas()
    if alaprajz[1][2] or alaprajz[0][1]:
        alaprajz[0][2] = szoba_sorsolas()
    if alaprajz[2][1] or alaprajz[1][2]:
        alaprajz[2][2] = szoba_sorsolas()
    if alaprajz[1][0] or alaprajz[2][1]:
        alaprajz[2][0] = szoba_sorsolas()

    # Elkészült az alaprajz, a hecc kedvéért ki is nyomtatjuk:
    for i in range(3):
        print(alaprajz[i])

    # Most jöhet a szobagyártás. Minden szobánál végig kell csekkolni,
    # hogy melyik szomszédjában van szoba, mert oda folyosó fog menni.
    szobak = []
    for j in range(3):
        for i in range(3):
            # Ha az i,j koordinátán van szoba, akkor ott megnézzük a
            # szomszédokat.
            if alaprajz[j][i]:
                szobastring = ""
                for k in range(4):
                    jk = j + szomszedok[k][0]
                    ik = i + szomszedok[k][1]
                    slot_exists = jk in range(3) and ik in range(3)
                    # Ha az adott szomszédban van szoba, akkor oda folyosó fog
                    # vezetni. Ilyenkor a szomszéd betűjele benne van a képfájl
                    # nevében, ezért ezt a betűt felírjuk.
                    if slot_exists and alaprajz[jk][ik]:
                        szobastring += szomszed_betuk[k]
                # Mindegyik fajta szobaképből három van. Ezek közül is véletlen-
                # szerűen választunk.
                szobastring += str(r.randint(1, 3))
                # A hecc kedvéért kinyomtatjuk a szobák generálásához használt
                # fileneveket is:
                print(i, j, szobastring + ".png")
                uj_szoba = pg.image.load("szobakepek/" + szobastring + ".png")
                uj_szoba_helye = uj_szoba.get_rect()
                # A szobák középpontját a játéktér középpontja, az i, j
                # koordinátáik és a méretük határozza meg. A méretüket
                # lekicsinyítettük 320x240-re, hogy biztosan elférjenek a
                # képernyőn. A kijelző közepét itt (480, 360)-nak vettük, de
                # lehet más is.
                uj_szoba_helye.centerx = 480 + (i-1) * 320
                uj_szoba_helye.centery = 360 + (j-1) * 240
                szobak.append((uj_szoba, uj_szoba_helye))

    # A szobák háttere (128, 128, 128) színű. Ezt a színt érdemes használni
    # a játék hátterének is, hogy ne üssenek el azok a részek,
    # ahol nincs szoba.
    return szobak

kijelzo = pg.display.set_mode((960,720))
szurke = (128, 128, 128)
szobak = gyarts_szobakat_legyszi()

while True:
    #kilepeshez
    for esemeny in pg.event.get():
        if esemeny.type == pg.QUIT:
            sys.exit()
    #kijelzohoz
    kijelzo.fill((128,128,128))
    for szoba in szobak:
        kijelzo.blit(*szoba)
    pg.display.flip()
