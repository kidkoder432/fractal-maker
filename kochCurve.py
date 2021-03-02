import turtle as t




kochSystem = 'h'
scr = t.Screen()
scr.screensize(10000, 10000)
t.colormode(255)
t.speed(0)


    

def line(startPos, length, color=(255, 255, 255)):
    t.pencolor(color)
    t.setpos(startPos)
    t.forward(length)

# 'd' means move down and right
# 'u' means move up and right
# 'h' means move horizontally to the right


def update(system):
    newSystem = ''
    for i in system:
        if i == 'h':
            newSystem += 'h+h--h+h'
        else:
            newSystem += i

    return newSystem



def drawKoch(system, dist):
    global currentPos
    for s in system:
        if s == '-':
            t.right(60)
        elif s == '+':
            t.left(60)
        elif s == 'h':
            line(currentPos, dist, (255, 128, 100))
        currentPos = t.pos()

distance = 5
t.ht()
t.bgcolor((0,0,0))



currentPos = (-5000, 0)
t.pu()
t.setpos(currentPos)
t.pd()

drawKoch(kochSystem, distance)   
currentPos = (-220, 0)
t.pu()
t.setpos(currentPos)
t.pd()
for i in range(5):
    kochSystem = update(kochSystem)




drawKoch(kochSystem, distance)         

ts = t.getscreen()
ts.getcanvas().postscript(file='kochcurve.eps')
print('done')


t.done()

