import pygame as pg
import sys
import random as r

def billentyuk_figyelese():
    pass

def kijelzo_frissitese():
    pass

def szinek_figyelese(x, y):
    kint_vagyunk_e = True
    for i in range(x-3, x+4):
        for e in range(y-3, y+4):
            if tuple(jatekter.get_at((i, e))) == (229, 229, 229, 255):
                kint_vagyunk_e = False
            else:
                szin = tuple(jatekter.get_at((i, e)))
    if kint_vagyunk_e == True:
        print(szin)
    return kint_vagyunk_e

meret =(1366, 768)
jatekter=pg.display.set_mode(meret, pg.FULLSCREEN)

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
                uj_szoba_helye.centerx = 683 + (i-1) * 320
                uj_szoba_helye.centery = 384 + (j-1) * 240
                szobak.append((uj_szoba, uj_szoba_helye))

    # A szobák háttere (128, 128, 128) színű. Ezt a színt érdemes használni
    # a játék hátterének is, hogy ne üssenek el azok a részek,
    # ahol nincs szoba.
    return szobak

"""
kozeppontok =  [(683, 384), (683, 134), (683, 634), (1083, 384), (283, 384),
    (1083, 634), (1083, 134), (283, 134), (283, 634)]
szobak = []
for i in range(9):
    if i == 0:
        sorsolas = random.randint(0, 1)
    else:
        sorsolas = random.randint(0, 2)
    if sorsolas < 2:
        if sorsolas == 0:
            uj_szoba = pg.image.load("szoba1.png")
        if sorsolas == 1:
            uj_szoba = pg.image.load("szoba2.png")
        uj_szoba_helye = uj_szoba.get_rect()
        szobak.append([uj_szoba, uj_szoba_helye])
        uj_szoba_helye.centerx = kozeppontok[i][0]+random.randint(-60, 60)
        uj_szoba_helye.centery = kozeppontok[i][1]+random.randint(-60, 60)
"""

szobak_sebx = 0
szobak_seby = 0

szobak = gyarts_szobakat_legyszi()
csavoka = pg.image.load("stickman.png")
csavoka_hely = csavoka.get_rect()
csavoka_hely.center = (683, 384)
hatterszin = (128, 128, 128)

while True:
    # billentyuk figyelese
    for esemeny in pg.event.get():
        if esemeny.type == pg.KEYDOWN:
            if esemeny.key == pg.K_ESCAPE:
                sys.exit()
            elif esemeny.key == pg.K_RIGHT:
                szobak_sebx = -1
            elif esemeny.key == pg.K_LEFT:
                szobak_sebx = 1
            elif esemeny.key == pg.K_UP:
                szobak_seby = 1
            elif esemeny.key == pg.K_DOWN:
                szobak_seby = -1
        elif esemeny.type == pg.KEYUP:
            if esemeny.key == pg.K_UP and szobak_seby == 1:
                szobak_seby = 0
            elif esemeny.key == pg.K_DOWN and szobak_seby == -1:
                szobak_seby = 0
            if esemeny.key == pg.K_RIGHT and szobak_sebx == -1:
                szobak_sebx = 0
            elif esemeny.key == pg.K_LEFT and szobak_sebx == 1:
                szobak_sebx = 0
    # kijelzo frissitese
    jatekter.fill(hatterszin)
    for szoba in szobak:
        if szobak_sebx < 0 and not jobbra_van_fal:
            szoba[1].centerx+= szobak_sebx
        elif szobak_sebx > 0 and not balra_van_fal:
            szoba[1].centerx+= szobak_sebx
        if szobak_seby > 0 and not fent_van_fal:
            szoba[1].centery+= szobak_seby
        elif szobak_seby < 0 and not lent_van_fal:
            szoba[1].centery+= szobak_seby
        jatekter.blit(*szoba)
    jobbra_van_fal = szinek_figyelese(688, 384)
    balra_van_fal = szinek_figyelese(677, 384)
    fent_van_fal = szinek_figyelese(683, 377)
    lent_van_fal = szinek_figyelese(683, 391)
    if szinek_figyelese(683, 384) == True:
        print("Ajjaj!")
    jatekter.blit(csavoka, csavoka_hely)
    pg.display.flip()
