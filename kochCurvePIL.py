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
# 'u' means right
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
    c = 0
    lines = str(len(system))
    for s in system:
        print(str(c)+ '/' + lines, end='\r')
        if s == '-':
            d -= 60
        elif s == '+':
            d += 60
        elif s == 'h':
            currentPos = line(currentPos, dist, d, (255, 228, 122))
        c += 1

kochSystem = 'h'
for i in range(7):
    kochSystem = update(kochSystem)

w = len(kochSystem) // 1893 * 739
h = len(kochSystem) // 7
distance = (len(kochSystem) / w) ** 2
currentPos = (0, 1)

print(w, h)
im = Image.new('RGB', (w, h))
draw = Draw(im)
drawKoch(kochSystem, distance)

im = im.transpose(Image.FLIP_TOP_BOTTOM)
print('ready')
im.save('kochCurve.jpeg')
