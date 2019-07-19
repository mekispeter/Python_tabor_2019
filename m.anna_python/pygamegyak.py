import pygame as pg
import sys

size=600,600
jatekter=pg.display.set_mode(size)
bckgrcolour=(255,255,255)

smiley=pg.image.load("smiley.png")
smiley_hely=smiley.get_rect()
smiley_hely.center=(300, 300)

xseb=0
yseb=0

while True:
    jatekter.fill(bckgrcolour)
    jatekter.blit(smiley, smiley_hely)
    pg.display.flip()
    for event in pg.event.get():
        if event.type==pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                sys.exit()
            if event.key==pg.K_RIGHT:
                xseb=3
            if event.key==pg.K_LEFT:
                xseb=-3
            if event.key==pg.K_UP:
                yseb=-3
            if event.key==pg.K_DOWN:
                yseb=3
        elif event.type==pg.KEYUP:
            if event.key==pg.K_RIGHT or event.key==pg.K_LEFT:
                xseb=0
            if event.key==pg.K_UP or event.key==pg.K_DOWN:
                yseb=0
    if smiley_hely.centerx>=size[0]:
        smiley_hely.centerx-=3
        xseb=0
    elif smiley_hely.centerx<=0:
        smiley_hely.centerx+=3
        xseb=0
    elif smiley_hely.centery<=0:
        smiley_hely.centery+=3
        yseb=0
    elif smiley_hely.centery>=size[1]:
        smiley_hely.centery-=3
        yseb=0

    smiley_hely.centerx+=xseb
    smiley_hely.centery+=yseb
