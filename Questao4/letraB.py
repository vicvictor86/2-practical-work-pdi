from PIL import Image

import sys        
sys.path.append('D:\Programming\PDI\Trabalho2')

from Questao3.letraC import diff
from Questao4.letraA import pixelInsideImage

def erosion(image, kernel):
    lines = image.size[0]
    columns = image.size[1]
    imageResult = image.copy()

    rangeToSearch = len(kernel) // 2

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
                        if kernel[xInMask][yInMask] == 0 and image.getpixel((i+k, j+l)) != 0:
                            result = 1           
                            imageResult.putpixel((i, j), result)
                    yInMask += 1
                xInMask += 1
            
    return imageResult

if __name__ == '__main__':
    image1 = Image.open("Trabalho2\Questao4\JImage.png")

    mask = {}
    mask[0] = [0, 0, 0] 
    mask[1] = [0, 0, 0] 
    mask[2] = [0, 0, 0]  

    sizeKernel = 3
    erosionImage = erosion(image1, mask)

    # erosionImage.show()
    erosionImage.save("Trabalho2\Questao4\letraB\imageResult.png")

    diffImage = diff(image1, erosionImage)
    
    diffImage.save("Trabalho2\Questao4\letraB\diffImage.png")