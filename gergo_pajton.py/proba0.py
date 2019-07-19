import pygame as pg
import sys, random, time
meret_x = 1370
meret_y = 700
jatekter = pg.display.set_mode((meret_x, meret_y))
def ellenseggyartas():
    if random.randint(1, 200)==3:
        ellensegek.append(Ellenseg())



def szereplokmoz():
    for ellenseg in ellensegek:
        if ellenseg.el:
            jatekter.blit(ellenseg.jelmez, ellenseg.hely)
            ellenseg.hely.centerx += ellenseg.sebesseg
            if ellenseg.hely.centerx < 0:
                ellenseg.el = False
    karakter.hely.centerx+=karakter.sebx
    karakter.hely.centery+=karakter.seby

def kijelzofrissites():
    jatekter.fill((255,255,255))
    for ellenseg in ellensegek:
        if ellenseg.el:
            jatekter.blit(ellenseg.jelmez, ellenseg.hely)
            jatekter.blit(karakter.jelmez, karakter.hely)
    pg.display.flip()

def billentyukfigyelese():
    jatekter.blit(karakter.jelmez, karakter.hely)
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
def kijfigyeles():
    if karakter.hely.centerx <= 0+meret_x/2:
        karakter.sebx=0
        karakter.hely.centerx += 2
    elif karakter.hely.centerx>=meret_x-:
        karakter.sebx=0
        karakter.hely.centerx += -1
    if karakter.hely.centery == 0+meret_y/2:
        karakter.seby=0
        karakter.hely.centery += 1

class Ellenseg():
    def __init__(self):
        self.jelmez=pg.image.load("bevkocsi.png")
        self.hely=self.jelmez.get_rect()
        self.meret=self.jelmez.get_size()
        self.hely.center=(meret_x-self.meret[0], random.randint(0, meret_y-self.meret[1]))
        self.sebesseg=-3
        self.el=True

class Karakter():
    def __init__(self):
        self.jelmez = pg.image.load("bastya.png")
        self.hely =self.jelmez.get_rect()
        self.hely.center = (500, 300)
        jatekter.blit(self.jelmez, self.hely)
        pg.display.flip()
        self.seby=0
        self.sebx=0

karakter=Karakter()

ellensegek=[]
while True:
    ellenseggyartas()
    kijelzofrissites()
    billentyukfigyelese()
    szereplokmoz()
