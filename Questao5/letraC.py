from PIL import Image

import sys        
sys.path.append('D:\Programming\PDI\Trabalho2')
from Questao5.letraA import isolateColor, convertToBinary
from Questao4.letraA import dilation
from Questao3.letraA import union
from Questao3.letraB import intersection
from Questao3.letraC import diff, areDifferent

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

def imageComplementary(image):
    lines = image.size[0]
    columns = image.size[1]
    newImage = image.copy()
    for i in range(lines):
        for j in range(columns):
            pixel = image.getpixel((i, j))
            if pixel == 0:
                newImage.putpixel((i, j), 1)
            else:
                newImage.putpixel((i, j), 0)
    return newImage

def complementBorder(image):
    lines = image.size[0]
    columns = image.size[1]
    newImage = image.copy()
    for i in range(lines):
        for j in range(columns):
            if i == 0 or i == lines - 1 or j == 0 or j == columns - 1:
                newImage.putpixel((i, j), 0)
            else:
                newImage.putpixel((i, j), 1)
    return newImage

def geodesicDilation(borderComplement, complementaryImage, structElement, structElementCenter):
    borderComplement = borderComplement.copy()
    complementaryImage = complementaryImage.copy()
    
    result_image = dilation(borderComplement, structElement, structElementCenter)
    result_image = intersection(result_image, complementaryImage)

    while areDifferent(result_image, borderComplement):
        borderComplement = result_image
        result_image = dilation(borderComplement, structElement, structElementCenter)
        result_image = intersection(result_image, complementaryImage)

    return diff(borderComplement, complementaryImage)

def putImagesTogether(images):
    lines = images[0].size[0]
    columns = images[0].size[1]
    newImage = Image.new("RGBA", (lines, columns), color = 'white')
    
    for image in images:
        for i in range(lines):
            for j in range(columns):
                pixel = image.getpixel((i, j))
                if pixel != (255, 255, 255, 255):
                    newImage.putpixel((i, j), pixel)

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
    mask3x3[0] = [1, 0, 1] 
    mask3x3[1] = [0, 0, 0] 
    mask3x3[2] = [1, 0, 1]  

    mask5x5 = {}
    mask5x5[0] = [0, 0, 0, 0, 0]
    mask5x5[1] = [0, 0, 0, 0, 0]
    mask5x5[2] = [0, 0, 0, 0, 0]
    mask5x5[3] = [0, 0, 0, 0, 0]
    mask5x5[4] = [0, 0, 0, 0, 0]

    # Blue Image
    onlyBlueImageBinary = convertToBinary(isolateColor(image1, blue))
    onlyBlueImageBinary.save("Trabalho2\Questao5\letraC\onlyBlueImage.png")

    onlyBlueImageComplementary = imageComplementary(onlyBlueImageBinary)
    onlyBlueImageComplementary.save("Trabalho2\Questao5\letraC\onlyBlueImageComplementary.png")

    blueComplementBorder = complementBorder(onlyBlueImageBinary)

    onlyBlueImageDiffFilledHoles = geodesicDilation(blueComplementBorder, onlyBlueImageComplementary, mask3x3, (1, 1))
    onlyBlueImageDiffFilledHoles.save("Trabalho2\Questao5\letraC\onlyBlueImageDiffFilledHoles.png")

    onlyBlueImageFilledHolesComplete = union(onlyBlueImageDiffFilledHoles, onlyBlueImageBinary)
    onlyBlueImageFilledHolesComplete.save("Trabalho2\Questao5\letraC\onlyBlueImageFilledHolesComplete.png")

    # Yellow Image
    onlyYellowImageBinary = convertToBinary(isolateColor(image1, yellow))
    onlyYellowImageBinary.save("Trabalho2\Questao5\letraC\onlyYellowImage.png")

    onlyYellowImageBinaryComplementary = imageComplementary(onlyYellowImageBinary)
    onlyYellowImageBinaryComplementary.save("Trabalho2\Questao5\letraC\onlyYellowImageComplementary.png")

    yellowComplementBorder = complementBorder(onlyYellowImageBinary)

    onlyYellowImageDiffFilledHoles = geodesicDilation(yellowComplementBorder, onlyYellowImageBinaryComplementary, mask3x3, (1, 1))
    onlyYellowImageDiffFilledHoles.save("Trabalho2\Questao5\letraC\onlyyellowImageDiffFilledHoles.png")

    onlyYellowImageFilledHolesComplete = union(onlyYellowImageDiffFilledHoles, onlyYellowImageBinary)
    onlyYellowImageFilledHolesComplete.save("Trabalho2\Questao5\letraC\onlyYellowImageFilledHolesComplete.png")
    
    # Red Image
    onlyRedImageBinary = convertToBinary(isolateColor(image1, red))
    onlyRedImageBinary.save("Trabalho2\Questao5\letraC\onlyRedImage.png")

    onlyRedImageBinaryComplementary = imageComplementary(onlyRedImageBinary)
    onlyRedImageBinaryComplementary.save("Trabalho2\Questao5\letraC\onlyRedImageComplementary.png")

    redComplementBorder = complementBorder(onlyRedImageBinary)

    onlyRedImageDiffFilledHoles = geodesicDilation(redComplementBorder, onlyRedImageBinaryComplementary, mask3x3, (1, 1))
    onlyRedImageDiffFilledHoles.save("Trabalho2\Questao5\letraC\onlyRedImageDiffFilledHoles.png")

    onlyRedImageFilledHolesComplete = union(onlyRedImageDiffFilledHoles, onlyRedImageBinary)
    onlyRedImageFilledHolesComplete.save("Trabalho2\Questao5\letraC\onlyRedImageFilledHolesComplete.png")

    # Green Image
    onlyGreenImageBinary = convertToBinary(isolateColor(image1, green))
    onlyGreenImageBinary.save("Trabalho2\Questao5\letraC\onlyGreenImage.png")

    onlyGreenImageBinaryComplementary = imageComplementary(onlyGreenImageBinary)
    onlyGreenImageBinaryComplementary.save("Trabalho2\Questao5\letraC\onlyGreenImageComplementary.png")

    greenComplementBorder = complementBorder(onlyGreenImageBinary)

    onlyGreenImageDiffFilledHoles = geodesicDilation(greenComplementBorder, onlyGreenImageBinaryComplementary, mask3x3, (1, 1))
    onlyGreenImageDiffFilledHoles.save("Trabalho2\Questao5\letraC\onlyGreenImageDiffFilledHoles.png")

    onlyGreenImageFilledHolesComplete = union(onlyGreenImageDiffFilledHoles, onlyGreenImageBinary)
    onlyGreenImageFilledHolesComplete.save("Trabalho2\Questao5\letraC\onlyGreenImageFilledHolesComplete.png")

    binaryBlueImageWithoutHoles = Image.open("Trabalho2\Questao5\letraC\onlyBlueImageFilledHolesComplete.png")
    binaryYellowImageWithoutHoles = Image.open("Trabalho2\Questao5\letraC\onlyYellowImageFilledHolesComplete.png")
    binaryRedImageWithoutHoles = Image.open("Trabalho2\Questao5\letraC\onlyRedImageFilledHolesComplete.png")
    binaryGreenImageWithoutHoles = Image.open("Trabalho2\Questao5\letraC\onlyGreenImageFilledHolesComplete.png")

    rgbBlueImage = convertToRGB(binaryBlueImageWithoutHoles, blue)
    rgbBlueImage.save("Trabalho2\Questao5\letraC\onlyBlueImageFilledHolesCompleteRGB.png")

    rgbTYellowImage = convertToRGB(binaryYellowImageWithoutHoles, yellow)
    rgbTYellowImage.save("Trabalho2\Questao5\letraC\onlyYellowImageFilledHolesCompleteRGB.png")

    rgbRedImage = convertToRGB(binaryRedImageWithoutHoles, red)
    rgbRedImage.save("Trabalho2\Questao5\letraC\onlyRedImageFilledHolesCompleteRGB.png")

    rgbGreenImage = convertToRGB(binaryGreenImageWithoutHoles, green)
    rgbGreenImage.save("Trabalho2\Questao5\letraC\onlyGreenImageFilledHolesCompleteRGB.png")
    
    originalImageWithoutHoles = putImagesTogether([rgbBlueImage, rgbTYellowImage, rgbRedImage, rgbGreenImage])
    originalImageWithoutHoles.save("Trabalho2\Questao5\letraC\originalImageWithoutHoles.png")
