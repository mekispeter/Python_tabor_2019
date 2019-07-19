import pygame as pg
import sys, random

pg.font.init()
size=1000,500
mode=int(input("Milyen nehéz legyen (1: nehéz, 2:közepes, 3: könnyű)?"))
jatekter=pg.display.set_mode(size)
bckgrcolour=(0, 80, 5)
myfont = pg.font.SysFont('Comic Sans MS', 30)

class Dagger():
    def __init__(self, pos):
        self.kep=pg.image.load("dagger.png")
        self.hely=self.kep.get_rect()
        self.hely.center=(pos)
        self.vis=1
        self.seb=2

class Hero():
    def __init__(self):
        self.kep=pg.image.load("goodknight.png")
        self.hely=self.kep.get_rect()
        self.hely.center=(0+self.kep.get_width()/2, 250)
        self.seb=0
        self.elet=3
        self.daggers=3

class Enemy():
    def __init__(self):
        self.kep=pg.image.load("darkknight.png")
        self.hely=self.kep.get_rect()
        self.hely.center=(size[0]-self.kep.get_width()/2, random.randint(0, size[1]))
        self.seb=-1
        self.el=1
darks=[Enemy() for i in range(4-mode)]
hero=Hero()
daggers=[]

def create_enemy():
    if random.randint(0, mode*100)==1:
        darks.append(Enemy())
def check_events():
    for event in pg.event.get():
        if event.type==pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                sys.exit()
            elif event.key==pg.K_UP:
                hero.seb=-1
            elif event.key==pg.K_DOWN:
                hero.seb=1
            elif event.key ==pg.K_SPACE and hero.daggers!=0:
                daggers.append(Dagger(hero.hely.center))
                hero.daggers-=1
        elif event.type==pg.KEYUP:
            if event.key==pg.K_UP or event.key==pg.K_DOWN:
                hero.seb=0
def update_screen():
    jatekter.fill(bckgrcolour)
    jatekter.blit(hero.kep,hero.hely)
    for dagger in daggers:
        if dagger.vis:
            jatekter.blit(dagger.kep,dagger.hely)
    for dark in darks:
        if dark.el:
            jatekter.blit(dark.kep,dark.hely)
    text1 = myfont.render('Életek: '+str(hero.elet), False, (0, 0, 0))
    text2=myfont.render('Daggers: '+str(hero.daggers), False, (0, 0, 0))
    jatekter.blit(text1,(0,0))
    jatekter.blit(text2,(0,20))
    pg.display.flip()
def move_sprites():
#kiment-e a jó a képernyőről
    if hero.hely.centery<=0:
        hero.hely.centery+=3
        hero.seb=0
    elif hero.hely.centery>=size[1]:
        hero.hely.centery-=3
        hero.seb=0
    hero.hely.centery+=hero.seb
#kiment-e a gonosz a képernyőről
    for dark in darks:
        if dark.el:
            dark.hely.centerx+=dark.seb
            if dark.hely.centerx<=0:
                dark.el=0
#dagger
    for dagger in daggers:
        if dagger.vis:
            dagger.hely.centerx+=dagger.seb
            if dagger.hely.centerx>=size[0]:
                dagger.vis=0

def detect_collision():
    for dark in darks:
        if hero.hely.colliderect(dark.hely):
            if dark.el:
                dark.el=0
                hero.elet-=1
            if hero.elet==0:
                print("GAME OVER!")
                sys.exit()
        for dagger in daggers:
            if dagger.hely.colliderect(dark.hely):
                if dark.el and dagger.vis:
                    dark.el=0
                    dagger.vis=0
                    hero.daggers+=1
while hero.elet!=0:
    create_enemy()
    check_events()
    move_sprites()
    update_screen()
    detect_collision()
