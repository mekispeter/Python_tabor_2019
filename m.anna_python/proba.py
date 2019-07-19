import time, random, math
x=0

hatar=30
deltax=1


while True:
    if deltax:
        print(" "*x, "# |0| #","     O")
    else:
        print(" "*x, "O    ", "# |0| #")
    if deltax:
        x+=1
    else:
        x+=-1
    if x==0:
        deltax=1
    if x==hatar:
        deltax=0
        hatar=random.randint(10, 100)
    time.sleep(0.07)
