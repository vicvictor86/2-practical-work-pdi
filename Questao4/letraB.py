from PIL import Image
import numpy as np 

from letraA import pixelInsideImage

def erosion(image, kernel):
    lines = image.size[0]
    columns = image.size[1]
    imageResult = image.copy()

    rangeToSearch = len(kernel) // 2

    for i in range(lines):
        for j in range(columns):
            xInMask = 0
            centralPixelValue = image.getpixel((i, j))
            
            #ta errado esse if tem que ser igual o valor central da máscara, dps corrigir
            if centralPixelValue != 0:
                continue

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
    sizeImage = 10
    image1 = Image.new("1", (sizeImage, sizeImage))
    image1.putdata(np.ones(sizeImage*sizeImage))

    for i in range(image1.size[0] // 2):
        for j in range(image1.size[1] // 2):
            image1.putpixel((i, j), 0)

    image1.save("Trabalho2\Questao4\letraB\image1.png")

    mask = {}
    mask[0] = [0, 0, 0] 
    mask[1] = [0, 0, 0] 
    mask[2] = [0, 0, 0]  

    sizeKernel = 3
    erosionImage = erosion(image1, mask)

    # erosionImage.show()
    erosionImage.save("Trabalho2\Questao4\letraB\imageResult.png")

    diffImage = Image.new("1", (sizeImage, sizeImage))
    for i in range(image1.size[0]):
        for j in range(image1.size[1]):
            diff = image1.getpixel((i, j)) - erosionImage.getpixel((i, j))
            diffImage.putpixel((i, j), diff)
    
    diffImage.save("Trabalho2\Questao4\letraB\diffImage.png")

    proveDiff = Image.new("1", (sizeImage, sizeImage))
    for i in range(image1.size[0]):
        for j in range(image1.size[1]):
            diff = diffImage.getpixel((i, j)) + erosionImage.getpixel((i, j))
            proveDiff.putpixel((i, j), diff)
    
    proveDiff.save("Trabalho2\Questao4\letraB\proveDiff.png")
