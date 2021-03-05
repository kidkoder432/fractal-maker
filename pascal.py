# Imports
import numpy as np
from PIL import Image

# Define some functions
def op(i):
    # Create Pascal's triangle
    layers.append([])
    for x in range(len(layers[i-1]) - 1):
        layers[-1].append(layers[i-1][x] + layers[i-1][x+1])


def drawPixel(fillOrOutline, outlineColor=(255, 255, 255, 255), fillColor=(0, 0, 0, 0)):
    # Choose which color to output.
    if fillOrOutline:
        return outlineColor
    return fillColor



# Get number of layers to draw
numLayers = int(input('How many layers? > '))

# Set up the layers
layers = [[0] * (numLayers * 2 + 1)]
layers[0][numLayers] = 1

# Create Pascal's triangle
for i in range(1, int(numLayers + 1)):
    op(i)

# Set up colors
fill = (0, 0, 0)
outline = (255, 228, 122)

# Create a counter and set up the new image
counter = 0
im = Image.new('RGB', (len(layers[-1]), len(layers)), fill)

# Draw the Sierpinski triangle
for i in layers:
    for num in i:
        if num == 0:
            i.remove(num) # Remove 0s because they will just be colored with the fill color 

        else:
            im.putpixel((i.index(num), layers.index(i)),
                        drawPixel(num % 2, outline, fill))
    print(counter)
    counter += 1

# This program only generates half of the triangle, so flip it and paste on the other side to make the whole triangle
flippedTriangle = im.crop(
    (0, 0, len(layers[-1]) // 2, len(layers))).transpose(Image.FLIP_LEFT_RIGHT)
im.paste(flippedTriangle, (len(layers[-1]) //
                           2, 0, len(layers[-1]) - 1, len(layers)))

# Save the triangle
im.save('triangle.jpeg')
