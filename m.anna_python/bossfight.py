import pygame as pg
import sys, math, random

clock=pg.time.Clock()
pg.font.init()
myfont = pg.font.SysFont('Comic Sans MS', 30)
size=500,700
screen=pg.display.set_mode(size)
black=(0,0,0)
white=(255, 255, 255)
blue=(0,0,255)
red=(255, 0, 0)

class Image():
    def __init__(self, kep, pos, type=1):
        self.kep=pg.image.load(kep)
        self.hely=self.kep.get_rect()
        self.hely.center=(pos)
        self.type=type
        self.mask=pg.mask.from_surface(self.kep)
class Ward():
    def __init__(self):
            self.kep=pg.image.load("shield.png")
            self.hely=self.kep.get_rect()
            self.hely.center=(size[0]/2, size[1]-100)
            self.vis=3
            self.wait=0
            self.mask=pg.mask.from_surface(self.kep)

class Hero():
    def __init__(self, type=1):
        if type==1:
            self.kep=pg.image.load("knight.png")
            self.elet=5
            self.feattime=0
            self.text="Use shield in: "
            self.feature=raiseshield
            self.att=1
            self.speed=1
        if type==0:
            self.kep=pg.image.load("sorcerer.png")
            self.elet=3
            self.feattime=0
            self.text="Cast fireball in: "
            self.feature=castball
            self.att=0
            self.speed=2
        if type==2:
            self.kep=pg.image.load("rogue.png")
            self.elet=3
            self.feattime=0
            self.text="Sprint in: "
            self.feature=sprint
            self.att=1
            self.speed=2
            self.sprint=0
        self.hely=self.kep.get_rect()
        self.hely.center=(size[0]/2, size[1]-self.kep.get_height())
        self.xseb=0
        self.yseb=0
        self.mask=pg.mask.from_surface(self.kep)
    def move(self):
        self.hely.centerx+=self.xseb
        self.hely.centery+=self.yseb
class Shield():
    def __init__(self, owner):
        self.kep=pg.image.load("shield.png")
        self.hely=self.kep.get_rect()
        self.hely.center=(owner.hely.center)
        self.owner=owner
        self.vis=0
        self.mask=pg.mask.from_surface(self.kep)
    def move(self):
        self.hely.center=(self.owner.hely.center)

class Boss():
    def __init__(self):
        self.kep=pg.image.load("boss.png")
        self.hely=self.kep.get_rect()
        self.hely.center=(size[0]/2, size[1]/4)
        self.elet=8
        self.feattime=random.randint(self.elet-1, self.elet+1)
        self.mask=pg.mask.from_surface(self.kep)
        self.waitflame=-1
        self.flames=[]
    def flamecircle(self):
        boss.waitflame=-2
        self.flames=[]
        b=int(self.hely.centerx-self.kep.get_width()/2)
        j=int(self.hely.centerx+self.kep.get_width()/2)
        f=int(self.hely.centery-self.kep.get_height()/2)
        l=int(self.hely.centery+self.kep.get_height()/2)
        for x in [b, j]:
            for y in range(f, l, 50):
                self.flames.append(Image("flame.png", (x,y)))
        for y in [f, l]:
            for x in range(b, j, 50):
                self.flames.append(Image("flame.png", (x,y)))
        self.flames.append(Image("flame.png", (j, l)))
        self.kep=pg.image.load("boss.png")
class Magicball():
    def __init__(self, caster, target):
        self.kep=pg.image.load("fireball.png")
        self.hely=self.kep.get_rect()
        self.hely.center=(caster.hely.center)
        self.seb=2
        self.vis=1
        self.target=target
        self.mask=pg.mask.from_surface(self.kep)
    def move(self):
        if self.vis:
            dx=self.target.hely.centerx-self.hely.centerx
            dy=self.target.hely.centery-self.hely.centery
            dist=math.sqrt(dx*dx+dy*dy)
            dx, dy = dx / dist, dy / dist
            self.hely.centerx += dx * self.seb
            self.hely.centery += dy * self.seb

#0-kezdés, 1-folyamatban, 2-győzelem, 3-vereség
gamestate=0
frame=0
message=["", 0]
hero=None
shield=None
tryagain=Image("try_again.png", (size[0]/2, size[1]/4*3))
ward=Ward()
boss=Boss()
moving=[]
fireballs=[]

def raiseshield(owner, target=None):
    if owner.feattime==0:
        shield.vis=3
def castball(owner, target=boss):
    if owner.feattime==0:
        fireball=Magicball(owner, target)
        fireballs.append(fireball)
        moving.append(fireball)
        owner.feattime=5
def sprint(owner, target=None):
    if owner.feattime==0:
        owner.speed=6
        owner.sprint=3

def selected(sprite):
    mx, my=pg.mouse.get_pos()
    if sprite.hely.collidepoint(mx, my):
        return True
    else:
        return False
def collide(a, b):
    offset_x = a.hely.right-b.hely.right
    offset_y = a.hely.bottom-b.hely.bottom
    overlap=a.mask.overlap(b.mask, (offset_x, offset_y))
    return overlap is not None
def pushback(pusher):
    if hero.hely.centery>pusher.hely.centery:
        hero.yseb=5
    else:
        hero.yseb=-5
    if hero.hely.centerx>pusher.hely.centerx:
        hero.xseb=1
    else:
        hero.xseb=-1

def chosehero():
    text=myfont.render("Chose your hero!", False, white)
    screen.fill(black)
    c0=Image("sorcerer.png", (size[0]/2-55, size[1]/2), type=0)
    c1=Image("knight.png", (size[0]/2, size[1]/2), type=1)
    c2=Image("rogue.png", (size[0]/2+58, size[1]/2), type=2)
    chars=[c0, c1, c2]
    for char in chars:
        screen.blit(char.kep, char.hely)
    screen.blit(text,(size[0]/2-text.get_width()/2,0))
    pg.display.flip()
    for event in pg.event.get():
        if event.type==pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                sys.exit()
        elif event.type==pg.MOUSEBUTTONDOWN:
            for char in chars:
                if selected(char):
                    global gamestate, moving, hero, shield, fireballs
                    if char.type==1:
                        hero=Hero(type=1)
                        shield=Shield(hero)
                        moving=[hero, shield]
                    elif char.type==0:
                        hero=Hero(type=0)
                        moving=[hero]
                    elif char.type==2:
                        hero=Hero(type=2)
                        moving=[hero]
                    boss.elet=8
                    ward.wait=0
                    if shield is not None:
                        shield.vis=0
                    fireballs=[]
                    gamestate=1

def move_blit():
        lives=myfont.render("Your lives: "+"O"*hero.elet, False, white)
        feattime=myfont.render(hero.text+str(hero.feattime), False, white)
        wardtime=myfont.render("Ward reappers in:"+str(ward.wait), False, white)
        bosslives=myfont.render("Boss's lives: "+"O"*boss.elet, False, white)
        messagetext=myfont.render(message[0], False, white)
        if hero.hely.centerx>=size[0]:
            hero.hely.centerx-=hero.speed
            xseb=0
        elif hero.hely.centerx<=0:
            hero.hely.centerx+=hero.speed
            xseb=0
        elif hero.hely.centery<=0:
            hero.hely.centery+=hero.speed
            yseb=0
        elif hero.hely.centery>=size[1]:
            hero.hely.centery-=hero.speed
            yseb=0
        for char in moving:
            char.move()
        screen.fill(black)
        for flame in boss.flames:
            screen.blit(flame.kep, flame.hely)
        screen.blit(boss.kep, boss.hely)
        if shield is not None:
            if shield.vis!=0:
                screen.blit(shield.kep, shield.hely)
        if ward.vis!=0:
            screen.blit(ward.kep, ward.hely)
        screen.blit(hero.kep, hero.hely)
        for fb in fireballs:
            if fb.vis:
                screen.blit(fb.kep, fb.hely)
        screen.blit(lives,(0,600))
        if hero.feattime!=0:
            screen.blit(feattime, (0, 630))
        if ward.wait!=0:
            screen.blit(wardtime, (size[0]-wardtime.get_width(), 600))
        screen.blit(bosslives,(0, 0))
        screen.blit(messagetext,(size[0]/2-messagetext.get_width()/2, size[1]/2))
        pg.display.flip()
def events():
    for event in pg.event.get():
        if event.type==pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                sys.exit()
            if event.key==pg.K_RIGHT:
                hero.xseb=hero.speed
            if event.key==pg.K_LEFT:
                hero.xseb=-hero.speed
            if event.key==pg.K_UP:
                hero.yseb=-hero.speed
            if event.key==pg.K_DOWN:
                hero.yseb=hero.speed
            if event.key==pg.K_SPACE:
                hero.feature(hero)
        elif event.type==pg.KEYUP:
            if event.key==pg.K_RIGHT or event.key==pg.K_LEFT:
                hero.xseb=0
            if event.key==pg.K_UP or event.key==pg.K_DOWN:
                hero.yseb=0
        elif event.type==pg.MOUSEBUTTONDOWN:
            used=0
            for fb in fireballs:
                if selected(fb):
                    hero.feature(hero, target=fb)
                    used=1
            if not used:
                hero.feature(hero)
def collisions():
    for fb in fireballs:
        if fb.vis:
            if shield is not None:
                if collide(fb, shield) and shield.vis!=0:
                    fb.vis=0
            if collide(fb, fb.target):
                if hasattr(fb.target, "elet"):
                    if fb.target==boss:
                        boss.waitflame=1
                        boss.kep=pg.image.load("boss2.png")
                    fb.target.elet-=1
                else:
                    fb.target.vis=0
                fb.vis=0
            if collide(fb, ward) and ward.vis!=0:
                if fb.target!=hero:
                    global message
                    message=["Can't shoot inside ward!", 2]
                fb.vis=0
                ward.vis-=1
                if ward.vis==0:
                    ward.wait=10
    if collide(hero, boss):
        boss.elet-=hero.att
        boss.waitflame=1
        boss.kep=pg.image.load("boss2.png")
        pushback(boss)
    for flame in boss.flames:
        if shield is not None:
            if collide(flame, hero) and shield.vis!=0:
                hero.elet-=1
                pushback(flame)
        else:
            if collide(flame, hero):
                hero.elet-=1
                pushback(flame)
def timetracker():
        global frame
        if frame%30==0:
            if boss.feattime!=0:
                boss.feattime-=1
            else:
                fireball=Magicball(boss, hero)
                fireballs.append(fireball)
                moving.append(fireball)
                boss.feattime=random.randint(boss.elet-1, boss.elet+1)
            if hasattr(shield, "vis"):
                if shield.vis!=0:
                    shield.vis-=1
                    if shield.vis==0:
                        hero.feattime=5
                elif hero.feattime!=0:
                    hero.feattime-=1
            elif hasattr(hero, "sprint"):
                if hero.sprint!=0:
                    hero.sprint-=1
                    if hero.sprint==0:
                        hero.speed=2
                        hero.feattime=5
                if hero.feattime!=0:
                    hero.feattime-=1
            else:
                if hero.feattime!=0:
                    hero.feattime-=1
            if ward.wait!=0:
                ward.wait-=1
                if ward.wait==0:
                    ward.vis=3
            global message
            if message[1]!=0:
                message[1]-=1
                if message[1]==0:
                    message=["", 0]
            if boss.waitflame>0:
                boss.waitflame-=1
            elif boss.waitflame<-1:
                boss.waitflame+=1
            elif boss.waitflame==0:
                boss.flamecircle()
            else:
                boss.flames=[]
        frame+=1
        clock.tick(30)
def quitgame():
    global gamestate
    if boss.elet==0:
        gamestate=2
    elif hero.elet==0:
        gamestate=3
def game():
    move_blit()
    events()
    collisions()
    timetracker()
    quitgame()

def endgame():
    global gamestate
    if gamestate==2:
        screen.fill(white)
        text=myfont.render("Victory!!!", False, blue)
    else:
        screen.fill(black)
        text=myfont.render("Defeat...", False, red)
    screen.blit(text, (size[0]/2-text.get_width()/2, size[1]/2))
    screen.blit(tryagain.kep, tryagain.hely)
    pg.display.flip()
    for event in pg.event.get():
        if event.type==pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                sys.exit()
        elif event.type==pg.MOUSEBUTTONDOWN:
            if selected(tryagain):
                gamestate=0

while True:
    if gamestate==0:
        chosehero()
    elif gamestate==1:
        game()
    elif gamestate==2 or gamestate==3:
        endgame()
