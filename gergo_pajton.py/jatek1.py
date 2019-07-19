import pygame as pg
import sys, math as m, random as r
meret_x=1366
meret_y=768
screen=pg.display.set_mode((meret_x, meret_y), pg.FULLSCREEN)
ora = pg.time.Clock()
class Karakter():
    def __init__(self):
        self.jelmez=pg.image.load("kor1.png")
        self.hely=self.jelmez.get_rect()
        self.hely.center=(meret_x/2, meret_y/2)
        self.meret=self.jelmez.get_size()
        self.szelesseg=self.meret[0]
        self.magassag=self.meret[1]
        self.sebx=0
        self.seby=0
        self.el=True
        screen.blit(self.jelmez, self.hely)
        pg.display.flip()
        print(self.meret)
karakter=Karakter()
class Haromszog():
    def __init__(self):
        self.jelmez=pg.image.load("haromszog.png")
        self.jelmez2=pg.image.load("haromszog.png")
        self.hely=self.jelmez.get_rect()
        self.meret=self.jelmez.get_size()
        self.szelesseg=self.meret[0]
        self.magassag=self.meret[1]
        self.latszik = False
haromszog=Haromszog()
def sorsolas(ell1, ell2): #ell1=szelesseg ell2=magassag
    maxy=meret_y-ell2/2
    maxx=meret_x-ell1/2
    miny=0+ell2/2
    minx=0+meret_x-ell1/2
    a=(r.randint(minx, maxx), miny)#sorsolas x1
    b=(r.randint(minx, maxx), maxy)#sorsolas x2
    c=(minx, r.randint(miny, maxy))#sorsolas y1
    d=(maxx, r.randint(miny, maxy))#sorsolas y2
    valasztas=r.randint(1, 4)
    if valasztas== 1:
        return(a)
    elif valasztas== 2:
        return(b)
    elif valasztas== 3:
        return(c)
    elif valasztas== 4:
        return(d)
class Ellenseg():
    def __init__(self):
        self.jelmez=pg.image.load("nyil1.png")
        self.hely=self.jelmez.get_rect()
        self.meret=self.jelmez.get_size()
        self.szelesseg=self.meret[0]
        self.magassag=self.meret[1]
        self.hely.center=sorsolas(self.szelesseg, self.magassag)
        self.sebx=0
        self.seby=0
        self.el=True
        screen.blit(self.jelmez, self.hely)
        pg.display.flip()
        self.befogox=karakter.hely.centerx-self.hely.centerx
        self.befogoy=karakter.hely.centery-self.hely.centery
        self.atfogo=m.sqrt(self.befogox**2+self.befogoy**2)
        self.sebesseg=self.atfogo/200
        self.sebx=self.befogox/self.sebesseg
        self.seby=self.befogoy/self.sebesseg
        if karakter.hely.centery > self.hely.centery:#fent
            if self.befogox < 0:
                self.szog=m.asin(self.befogox*-1/self.atfogo)/m.pi*180
            else:
                self.szog=m.asin(self.befogox/self.atfogo)/m.pi*180
            self.fl="l"
        else: #lent
            if self.befogox < 0:
                self.szog=m.asin(self.befogox*-1/self.atfogo)/m.pi*180
            else:
                self.szog=m.asin(self.befogox/self.atfogo)/m.pi*180
            self.fl="f"


        if karakter.hely.centerx > self.hely.centerx:
            self.jb="j"
        else:
            self.jb="b"

        if self.jb=="b" and self.fl=="f": #minusz x fok
            self.jelmez = pg.transform.rotate(self.jelmez, -1*self.szog)
        elif self.jb=="b"and self.fl=="l": #180 + x fok
            self.jelmez = pg.transform.rotate(self.jelmez, 180+self.szog)
        elif self.jb=="j" and self.fl=="f": #x fok
            self.jelmez = pg.transform.rotate(self.jelmez, self.szog)
        elif self.jb=="j" and self.fl=="l": #180-xfok
            self.jelmez = pg.transform.rotate(self.jelmez, 180-self.szog)
        print("helloworld", self.el)
ellenseg=Ellenseg()
ellensegek=[]
def ellenseggyartas():
    if r.randint(1,200)==2:
        ellensegek.append(Ellenseg())

def iranyitas():
    for esemeny in pg.event.get():
        if esemeny.type==pg.QUIT:
            sys.exit()
        elif esemeny.type==pg.KEYDOWN:
            if esemeny.key==pg.K_ESCAPE:
                sys.exit()
            elif esemeny.key==pg.K_RIGHT:
                karakter.sebx = 5
            elif esemeny.key==pg.K_LEFT:
                karakter.sebx=-5
            elif esemeny.key==pg.K_DOWN:
                karakter.seby=5
            elif esemeny.key==pg.K_UP:
                karakter.seby=-5
        elif esemeny.type==pg.KEYUP:
            if esemeny.key==pg.K_RIGHT or esemeny.key==pg.K_LEFT:
                karakter.sebx=0
            elif esemeny.key==pg.K_DOWN or esemeny.key==pg.K_UP:
                karakter.seby=0
def mozgatas():
    screen.fill((255,255,255))
    karakter.hely.centerx+=karakter.sebx
    karakter.hely.centery+=karakter.seby
    screen.blit(karakter.jelmez, karakter.hely)
    for ellenseg in ellensegek:
        maxx=meret_x-ellenseg.szelesseg/2
        maxy=meret_y-ellenseg.magassag/2
        minx=0+meret_x-ellenseg.szelesseg/2
        miny=0+ellenseg.magassag/2
        if ellenseg.hely.centerx > maxx+1 or ellenseg.hely.centerx < minx-1 or ellenseg.hely.centery > maxy+1 or ellenseg.hely.centery < miny-1:
            ellenseg.el=False
        if ellenseg.el:
            ellenseg.hely.centerx+=ellenseg.sebx
            ellenseg.hely.centery+=ellenseg.seby
            screen.blit(ellenseg.jelmez, ellenseg.hely)
    if haromszog.latszik:
        screen.blit(haromszog.jelmez2, haromszog.hely)
    pg.display.flip()

def kimenetel():
    if karakter.hely.centerx>meret_x+karakter.szelesseg/2:
        haromszog.hely.centery=karakter.hely.centery
        haromszog.hely.centerx=meret_x-haromszog.szelesseg/2
        haromszog.jelmez2 = pg.transform.rotate(haromszog.jelmez, 90)
        haromszog.latszik = True
    elif karakter.hely.centerx<0-karakter.szelesseg/2:
        haromszog.hely.centery=karakter.hely.centery
        haromszog.hely.centerx=0+haromszog.szelesseg/2
        haromszog.jelmez2 = pg.transform.rotate(haromszog.jelmez, -90)
        haromszog.latszik = True
    elif karakter.hely.centery>meret_y+karakter.magassag/2:
        haromszog.hely.centerx=karakter.hely.centerx
        haromszog.hely.centery=meret_y-haromszog.magassag/2
        haromszog.latszik = True
        haromszog.jelmez2 = haromszog.jelmez
    elif karakter.hely.centery<0-karakter.magassag/2:
        haromszog.hely.centerx=karakter.hely.centerx
        haromszog.hely.centery=0+haromszog.magassag/2
        haromszog.jelmez2 = pg.transform.rotate(haromszog.jelmez, 180)
        haromszog.latszik = True
    else:
        haromszog.latszik = False


while karakter.el:
    ellenseggyartas()
    mozgatas()
    iranyitas()
    kimenetel()
    ora.tick(60)
