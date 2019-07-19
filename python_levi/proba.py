import pygame as pg
import sys
meret=(850,700)
jatekter=pg.display.set_mode(meret)

ko_jelmez=pg.image.load("ko.png")
ko_hely=ko_jelmez.get_rect()
ko_hely.center=(300, 300)
ko_sebesseg=1

hatterszin=(30, 30, 70)

while 1+1 == 2:
    jatekter.fill(hatterszin)
    jatekter.blit(ko_jelmez,ko_hely)
    pg.display.flip()
    ko_hely.centerx+=ko_sebesseg
    if ko_hely.centerx>960:
        ko_sebesseg=-1
    if ko_hely.centerx<0:
        ko_sebesseg=1
    for esemeny in pg.event.get():
         if esemeny.type == pg.KEYDOWN:
             if esemeny.key == pg.K_ESCAPE:
                 sys.exit()
