from PIL import Image

import sys

sys.path.append('D:\Programming\PDI\Trabalho2')
from AuxFunctions.diff import diff        

def pixelInsideImage(image, i, j):
    lines = image.size[0]
    columns = image.size[1]
    if i < lines and i >= 0 and j < columns and j >= 0:
        return True
    return False

def dilation(image, structuralElement, structuralElementCenter=None):
    if structuralElementCenter is None:
        structuralElementCenter = len(structuralElement) // 2
        
    lines = image.size[0]
    columns = image.size[1]
    imageResult = image.copy()
    
    for i in range(lines):
        for j in range(columns):
            centralPixelValue = image.getpixel((i, j))
            if centralPixelValue == 255:
                centralPixelValue = 1
            centralPixelMask = structuralElement[structuralElementCenter][structuralElementCenter]
            
            # print(centralPixelValue, centralPixelMask)
            if centralPixelValue != centralPixelMask:
                continue
            
            xInMask = 0
            for k in range(-structuralElementCenter, structuralElementCenter + 1):
                yInMask = 0
                for l in range(-structuralElementCenter, structuralElementCenter + 1):
                    if pixelInsideImage(image, i+k, j+l):
                        if structuralElement[xInMask][yInMask] == 0:
                            result = 0           
                            imageResult.putpixel((i+k, j+l), result)
                    yInMask += 1
                xInMask += 1
            
    return imageResult

if __name__ == '__main__':
    mask = {}
    mask[0] = [0, 0, 0] 
    mask[1] = [0, 0, 0] 
    mask[2] = [0, 0, 0]  

    image1 = Image.open("Trabalho2\Questao4\JImage.png")

    dilationImage = dilation(image1, mask)

    dilationImage.save("Trabalho2\Questao4\letraA\imageResult.png")

    diffImage = diff(dilationImage, image1)
    
    diffImage.save("Trabalho2\Questao4\letraA\diffImage.png")
