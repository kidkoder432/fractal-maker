from PIL import Image
from PIL.ImageDraw import Draw
import math as m


def ptc(dist, theta):
    xc = m.cos(theta * (m.pi/180)) * dist
    yc = m.sin(theta * (m.pi/180)) * dist
    return (xc, yc)


def line(startPos, length, direction, color=(255, 255, 255)):
    coords = ptc(length, direction)
    end = tuple(sum(x) for x in zip(startPos, coords))
    draw.line((startPos + end), color)

    return end

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
    d = 0
    for s in system:
        if s == '-':
            d -= 60
        elif s == '+':
            d += 60
        elif s == 'h':
            currentPos = line(currentPos, dist, d, (255, 228, 122))


kochSystem = 'h'
for i in range(7):
    kochSystem = update(kochSystem)

distance = 6
w = len(kochSystem) // 23 * 10
h = len(kochSystem) // 8
currentPos = (w // 64, h // 7)

print(w, h)
im = Image.new('RGB', (w, h))
draw = Draw(im)
drawKoch(kochSystem, distance)

im = im.transpose(Image.FLIP_TOP_BOTTOM)
im.show()
im.save('kochCurve.png')
