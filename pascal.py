import numpy as np
from PIL import Image

def op(i):
    layers.append([])
    for x in range(len(layers[i-1]) - 1):
        layers[-1].append(layers[i-1][x] + layers[i-1][x+1])


def drawPixel(blackOrWhite, outlineColor=(255, 255, 255, 255), fillColor=(0, 0, 0, 0)):
    if blackOrWhite:
        return outlineColor
    return fillColor


numLayers = int(input('How many layers? > '))

layers = [[0] * (numLayers * 2 + 1)]
layers[0][numLayers] = 1

for i in range(1, int(numLayers + 1)):
    op(i)

# for i in layers:
#     for j in i:
#         if j == 0:
#            # print(j, end=' ')
#            i.remove(j)
#     # print()

fill = (0, 0, 0, 255)
outline = (255, 228, 122, 255)

counter = 0
pixels = []
im = Image.new('RGBA', (len(layers[-1]), len(layers)), fill)
for i in layers:
    pixels.append([])
    for num in i:
        if num == 0:
            i.remove(num)

        else:
            im.putpixel((i.index(num), layers.index(i)), drawPixel(num % 2, outline, fill))
            pass
        # pixels[-1].append(list(drawPixel(num % 2)))
    print(counter)
    counter += 1
# print(pixels, pixels[0])
# im=Image.fromarray(np.array(pixels, dtype='uint8'))
flippedTriangle=im.crop(
    (0, 0, len(layers[-1]) // 2, len(layers))).transpose(Image.FLIP_LEFT_RIGHT)
im.paste(flippedTriangle, (len(layers[-1]) //
                           2, 0, len(layers[-1]) - 1, len(layers)))

im.save('triangle.png')
