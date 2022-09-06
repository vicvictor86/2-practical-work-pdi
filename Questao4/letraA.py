from PIL import Image
import numpy as np 

import sys        
sys.path.append('D:\Programming\PDI\Trabalho2')
from Questao3.letraA import union

def pixelInsideImage(image, i, j):
    lines = image.size[0]
    columns = image.size[1]
    if i < lines and i >= 0 and j < columns and j >= 0:
        return True
    return False

def dilation(image, kernel):
    lines = image.size[0]
    columns = image.size[1]
    imageResult = image.copy()
    
    rangeToSearch = len(kernel) // 2
    result = 1
    
    for i in range(lines):
        for j in range(columns):
            centralPixelValue = image.getpixel((i, j))
            centralPixelMask = kernel[rangeToSearch][rangeToSearch]

            if centralPixelValue != centralPixelMask:
                continue
            
            xInMask = 0
            for k in range(-rangeToSearch, rangeToSearch + 1):
                yInMask = 0
                for l in range(-rangeToSearch, rangeToSearch + 1):
                    if pixelInsideImage(image, i+k, j+l):
                        if kernel[xInMask][yInMask] == 0:
                            result = 0           
                            
                        imageResult.putpixel((i+k, j+l), result)
                    yInMask += 1
                xInMask += 1
            
    return imageResult

if __name__ == '__main__':
    sizeImage = 10
    image1 = Image.new("1", (sizeImage, sizeImage))
    image1.putdata(np.ones(sizeImage*sizeImage))

    for i in range(image1.size[0] // 2):
        for j in range(image1.size[1] // 2):
            image1.putpixel((i, j), 0)

    image1.save("Trabalho2\Questao4\letraA\image1.png")

    mask = {}
    mask[0] = [0, 0, 0] 
    mask[1] = [0, 0, 0] 
    mask[2] = [0, 0, 0]  

    sizeKernel = 3
    dilationImage = dilation(image1, mask)

    # dilationImage.show()
    dilationImage.save("Trabalho2\Questao4\letraA\imageResult.png")

    diffImage = Image.new("1", (sizeImage, sizeImage))
    for i in range(image1.size[0]):
        for j in range(image1.size[1]):
            diff = image1.getpixel((i, j)) - dilationImage.getpixel((i, j))
            diffImage.putpixel((i, j), diff)
    
    diffImage.save("Trabalho2\Questao4\letraA\diffImage.png")

    proveDiff = Image.new("1", (sizeImage, sizeImage))
    for i in range(image1.size[0]):
        for j in range(image1.size[1]):
            diff = diffImage.getpixel((i, j)) + dilationImage.getpixel((i, j))
            proveDiff.putpixel((i, j), diff)
    
    proveDiff.save("Trabalho2\Questao4\letraA\proveDiff.png")
