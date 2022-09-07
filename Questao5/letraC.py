from PIL import Image
import numpy as np 

import sys        
sys.path.append('D:\Programming\PDI\Trabalho2')
from Questao5.letraA import isolateColor, convertToBinary

def searchInEveryDirectionsForPixelObject(image, i, j):
    isHole = True
    lines = image.size[0]
    columns = image.size[1]

    k = i
    while k < lines and isHole:
        pixel = image.getpixel((k, j))
        k += 1
        if pixel == 0:
            break
        if k >= lines:
            isHole = False
    
    k = i
    while k >= 0 and isHole:
        pixel = image.getpixel((k, j))
        if pixel == 0:
            break
        k -= 1
        if k < 0:
            isHole = False
    
    l = j
    while l < columns and isHole:
        pixel = image.getpixel((i, l))
        if pixel == 0:
            break
        l += 1
        if l >= columns:
            isHole = False

    l = j
    while l >= 0 and isHole:
        pixel = image.getpixel((i, l))
        if pixel == 0:
            break
        l -= 1
        if l < 0:
            isHole = False
    
    return isHole

def findPixelInsideBorder(image, listTeste):
    lines = image.size[0]
    columns = image.size[1]

    insideBorderCordinates = ()

    for i in range(lines):
        isInsideObject = False
        couldBeHole = False
        for j in range(columns):
            pixel = image.getpixel((i, j))
            pixelsCoordinates = (i, j)

            if pixel == 0 and not isInsideObject:
                isInsideObject = True
            if pixel == 1 and isInsideObject:
                couldBeHole = True

            if couldBeHole:
                isHole = searchInEveryDirectionsForPixelObject(image, i, j)

                if isHole:
                    insideBorderCordinates = pixelsCoordinates

                    return insideBorderCordinates
                else:
                    couldBeHole = False
                    isInsideObject = False

    
    return None

def convertToRGB(image, color):
    lines = image.size[0]
    columns = image.size[1]
    newImage = Image.new("RGBA", (lines, columns), color = 'white')
    for i in range(lines):
        for j in range(columns):
            pixel = image.getpixel((i, j))
            if pixel == 0:
                newImage.putpixel((i, j), color)
    return newImage


if __name__ == '__main__':
    black = (0, 0, 0, 255)
    white = (255, 255, 255, 255)
    red = (255, 0, 0, 255)
    green = (0, 255, 0, 255)
    blue = (0, 0, 255, 255)
    yellow = (255, 255, 0, 255)

    image1 = Image.open("Trabalho2\Questao5\quadro.png")

    mask3x3 = {}
    mask3x3[0] = [0, 0, 0] 
    mask3x3[1] = [0, 0, 0] 
    mask3x3[2] = [0, 0, 0]  

    mask5x5 = {}
    mask5x5[0] = [0, 0, 0, 0, 0]
    mask5x5[1] = [0, 0, 0, 0, 0]
    mask5x5[2] = [0, 0, 0, 0, 0]
    mask5x5[3] = [0, 0, 0, 0, 0]
    mask5x5[4] = [0, 0, 0, 0, 0]

    onlyBlueImage = convertToBinary(isolateColor(image1, blue))
    onlyBlueImage.save("Trabalho2\Questao5\letraC\onlyBlueImage.png")

    blueImageWithoutHoles = convertToRGB(onlyBlueImage, blue)
    
    blueImageWithoutHoles.save("Trabalho2\Questao5\letraC\\bluImageWithoutHoles.png")


    # diff(blueCirclesWithoutHoles3x3, onlyBlueImage).save("Trabalho2\Questao5\letraC\\blueCirclesWithoutHolesWith3x3Diff.png")

    # blueCirclesWithoutHoles5x5 = fillHoles(onlyBlueImage, mask5x5)
    # blueCirclesWithoutHoles5x5.save("Trabalho2\Questao5\letraA\\blueCirclesWithoutHolesWith5x5.png")

