from PIL import Image

import sys

sys.path.append('D:\Programming\PDI\Trabalho2')
from Questao4.letraD import closing        
from AuxFunctions.diff import diff

def fillHoles(image, structuringElement):
    return closing(image, structuringElement)

def isolateColor(image, color):
    lines = image.size[0]
    columns = image.size[1]
    newImage = Image.new(image.mode, (lines, columns), color = 'white')

    for i in range(lines):
        for j in range(columns):
            pixel = image.getpixel((i, j))
            if pixel == color:
                newImage.putpixel((i, j), color)

    return newImage

def convertToBinary(image):
    lines = image.size[0]
    columns = image.size[1]
    newImage = Image.new("1", (lines, columns), color = 'white')

    for i in range(lines):
        for j in range(columns):
            pixel = image.getpixel((i, j))
            if pixel != (255, 255, 255, 255):
                newImage.putpixel((i, j), 0)
            else:
                newImage.putpixel((i, j), 1)

    return newImage

if __name__ == '__main__':
    black = (0, 0, 0, 255)
    white = (255, 255, 255, 255)
    red = (255, 0, 0, 255)
    green = (0, 255, 0, 255)
    blue = (0, 0, 255, 255)
    yellow = (255, 255, 0, 255)

    image1 = Image.open("Trabalho2\Questao5\quadro.png")

    structuringElement3x3 = {}
    structuringElement3x3[0] = [0, 0, 0] 
    structuringElement3x3[1] = [0, 0, 0] 
    structuringElement3x3[2] = [0, 0, 0]  

    structuringElement5x5 = {}
    structuringElement5x5[0] = [0, 0, 0, 0, 0]
    structuringElement5x5[1] = [0, 0, 0, 0, 0]
    structuringElement5x5[2] = [0, 0, 0, 0, 0]
    structuringElement5x5[3] = [0, 0, 0, 0, 0]
    structuringElement5x5[4] = [0, 0, 0, 0, 0]

    onlyBlackImage = convertToBinary(isolateColor(image1, black))
    onlyBlackImage.save("Trabalho2\Questao5\letraA\onlyBlackImage.png")

    blackCirclesWithoutHoles3x3 = fillHoles(onlyBlackImage, structuringElement3x3)
    blackCirclesWithoutHoles3x3.save("Trabalho2\Questao5\letraA\\blackCirclesWithoutHolesWith3x3.png")

    diff(blackCirclesWithoutHoles3x3, onlyBlackImage).save("Trabalho2\Questao5\letraA\\blackCirclesWithoutHolesWith3x3Diff.png")

    blackCirclesWithoutHoles5x5 = fillHoles(onlyBlackImage, structuringElement5x5)
    blackCirclesWithoutHoles5x5.save("Trabalho2\Questao5\letraA\\blackCirclesWithoutHolesWith5x5.png")

    diff(blackCirclesWithoutHoles5x5, onlyBlackImage).save("Trabalho2\Questao5\letraA\\blackCirclesWithoutHolesWith5x5Diff.png")
