from PIL import Image

import sys        
sys.path.append('D:\Programming\PDI\Trabalho2')

from Questao3.letraC import diff
from Questao4.letraA import pixelInsideImage

def erosion(image, structuralElement):
    lines = image.size[0]
    columns = image.size[1]
    imageResult = image.copy()

    rangeToSearch = len(structuralElement) // 2
    # te = 0

    for i in range(lines):
        for j in range(columns):
            centralPixelValue = image.getpixel((i, j))
            centralPixelstructuralElement = structuralElement[rangeToSearch][rangeToSearch]

            if centralPixelValue != centralPixelstructuralElement:
                continue
            
            erosionHit = False
            
            xInstructuralElement = 0
            for k in range(-rangeToSearch, rangeToSearch + 1):
                yInstructuralElement = 0
                for l in range(-rangeToSearch, rangeToSearch + 1):
                    if pixelInsideImage(image, i+k, j+l):
                        if structuralElement[xInstructuralElement][yInstructuralElement] != image.getpixel((i+k, j+l)):
                            result = 1           
                            # te += 1
                            imageResult.putpixel((i, j), result)
                            erosionHit = True
                            break
                    yInstructuralElement += 1
                xInstructuralElement += 1

                if erosionHit:
                    break
            
    # print(te)
    return imageResult

if __name__ == '__main__':
    image1 = Image.open("Trabalho2\Questao4\JImage.png")

    estructuralElement = {}
    estructuralElement[0] = [0, 0, 0] 
    estructuralElement[1] = [0, 0, 0] 
    estructuralElement[2] = [0, 0, 0]  

    sizestructuralElement = 3
    erosionImage = erosion(image1, estructuralElement)
    
    # erosionImage.show()
    erosionImage.save("Trabalho2\Questao4\letraB\imageResult.png")

    diffImage = diff(image1, erosionImage)
    
    diffImage.save("Trabalho2\Questao4\letraB\diffImage.png")