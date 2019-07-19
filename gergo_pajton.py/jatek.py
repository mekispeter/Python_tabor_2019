import pygame as pg
import sys, random as r, time, math as m, time as t
meret_x = 1370
meret_y = 700
jatekter = pg.display.set_mode((meret_x, meret_y))

el = True

def ellenseggyartas():
    if r.randint(1, 300)==3:
        ellensegek.append(Ellenseg())

class Karakter():
    def __init__(self):
        self.jelmez=pg.image.load("kor1.png")
        self.hely=self.jelmez.get_rect()
        self.hely.center=(meret_x/2, meret_y/2)
        self.meret=self.jelmez.get_size()
        jatekter.blit(self.jelmez, self.hely)
        pg.display.flip()
        self.sebx=0
        self.seby=0
karakter=Karakter()
def sorsolas(ell):
    min_x = 0+ell[0]//2
    min_y = 0+ell[1]//2
    max_x = meret_x-ell[0]//2
    max_y = meret_y-ell[1]//2
    print(min_x, min_y, max_x, max_y)
    a=(r.randint(min_x, max_x), min_y)#x
    b=(min_x, r.randint(min_y, max_y))#y
    c=(r.randint(min_x, max_x), max_y)#x
    d=(max_x,r.randint(min_y, max_y))#y
    kesz=r.randint(1,4)
    if kesz == 1:
        return(a)
    elif kesz == 2:
        return(b)
    elif kesz == 3:
        return(c)
    elif kesz == 4:
        return(d)

class Ellenseg():
    def __init__(self):
        self.jelmez=pg.image.load("nyil1.png")
        self.meret=self.jelmez.get_size()
        self.hely=self.jelmez.get_rect()
        self.hely.center=sorsolas(self.meret)
        jatekter.blit(self.jelmez, self.hely)
        pg.display.flip()
        self.sebx=0
        self.seby=0
        self.el=True
        self.kulombsegx=karakter.hely.centerx-self.hely.centerx
        self.kulombsegy=karakter.hely.centery-self.hely.centery
        self.holvagyokx = self.hely.centerx
        self.holvagyoky = self.hely.centery
        if self.hely.centerx > karakter.hely.centerx:
            self.jb="j"
            self.x="-"
        else:
            self.jb="b"
            self.x="+"
        if self.hely.centery > karakter.hely.centery:
            self.y="-"
            self.szog=m.asin(self.kulombsegx*-1/m.sqrt(self.kulombsegx**2+self.kulombsegy**2))/m.pi*180
            self.fl="l"

        else:
            self.szog=m.asin(self.kulombsegy/m.sqrt(self.kulombsegx**2+self.kulombsegy**2))/m.pi*180
            self.fl="f"
            self.y="+"
        self.sebesseg=m.sqrt(self.kulombsegx**2+self.kulombsegy**2)/500
        self.oszto=m.sqrt(self.kulombsegx**2+self.kulombsegy**2)/self.sebesseg
        #self.sebx=self.kulombsegx/self.oszto
        #self.seby=self.kulombsegy/self.oszto
        self.sebx=self.kulombsegx/500
        self.seby=self.kulombsegy/500
        print(self.fl, self.jb)
        if self.jb=="j" and self.fl=="f":   #jobbra x fok
            self.jelmez = pg.transform.rotate(self.jelmez, int(self.szog))
        elif self.jb =="j" and self.fl=="l":    #jobbra 180 - x fok
            self.jelmez = pg.transform.rotate(self.jelmez, 180-int(self.szog))
        elif self.jb =="b" and self.fl=="f":     #jobbra -x fok
            self.jelmez = pg.transform.rotate(self.jelmez, -1*int(self.szog))
        elif self.jb=="b" and self.fl=="l":      # jobbra 180 + x fok
            self.jelmez = pg.transform.rotate(self.jelmez, 180+int(self.szog))
        print(self.hely.center, self.sebx, self.seby, self.szog, "fok")




ellenseg=Ellenseg()
ellensegek=[]
class Eletek():
    def __init__(self):
        self.darab=5

eletek=Eletek()


def kijelzofrissites():
    jatekter.fill((255,255,255))
    karakter.hely.centerx+=karakter.sebx
    karakter.hely.centery+=karakter.seby
    jatekter.blit(karakter.jelmez, karakter.hely)
    for ellenseg in ellensegek:
        jobbra_kint = ellenseg.hely.centerx > meret_x-ellenseg.meret[0]/2
        balra_kint = ellenseg.hely.centerx < 0+ellenseg.meret[0]/2
        felfele_kint = ellenseg.hely.centery < 0+ellenseg.meret[1]/2
        lefele_kint = ellenseg.hely.centery > meret_y-ellenseg.meret[1]/2
        if jobbra_kint or balra_kint or lefele_kint or felfele_kint:
            ellenseg.el=False
        if ellenseg.el:
            ellenseg.holvagyokx += ellenseg.sebx
            ellenseg.holvagyoky += ellenseg.seby
            ellenseg.hely.centerx = ellenseg.holvagyokx
            ellenseg.hely.centery = ellenseg.holvagyoky
            print(ellenseg.hely.center, "itt vagyok")
            jatekter.blit(ellenseg.jelmez, ellenseg.hely)
    pg.display.flip()

def kifigyeles():
    if karakter.hely.centerx == 0+karakter.meret[0]/2:
        karakter.sebx=0
        karakter.hely.centerx += 1
    elif karakter.hely.centerx==meret_x-karakter.meret[0]/2:
        karakter.sebx=0
        karakter.hely.centerx += -1
    elif karakter.hely.centery == 0+karakter.meret[1]/2:
        karakter.seby=0
        karakter.hely.centery += 1
    elif karakter.hely.centery == meret_y-karakter.meret[1]/2:
        karakter.seby=0
        karakter.hely.centery += -1

def iranyitas():
    for esemeny in pg.event.get():
        if esemeny.type == pg.QUIT:
            sys.exit()
        elif esemeny.type == pg.KEYDOWN:
            if esemeny.key == pg.K_ESCAPE:
                sys.exit()
            elif esemeny.key == pg.K_RIGHT:
                karakter.sebx=5
            elif esemeny.key == pg.K_LEFT:
                karakter.sebx=-5
            elif esemeny.key == pg.K_UP:
                karakter.seby=-5
            elif esemeny.key == pg.K_DOWN:
                karakter.seby=5
        elif esemeny.type == pg.KEYUP:
            if esemeny.key == pg.K_LEFT or esemeny.key == pg.K_RIGHT:
                karakter.sebx=0
            elif esemeny.key == pg.K_UP or esemeny.key == pg.K_DOWN:
                karakter.seby=0

while el:
    iranyitas()
    kijelzofrissites()
    ellenseggyartas()
