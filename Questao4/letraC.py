from PIL import Image
import numpy as np 

from letraA import dilation
from letraB import erosion

def opening(image, kernel):
    erosionImage = erosion(image, kernel)
    erosionImage.save("Trabalho2\Questao4\letraC\erosionImage.png")

    openingImage = dilation(erosionImage, kernel)
    openingImage.save("Trabalho2\Questao4\letraC\openingImage.png")
    
    return openingImage

if __name__ == '__main__':
    sizeImage = 10
    image1 = Image.new("1", (sizeImage, sizeImage))
    image1.putdata(np.ones(sizeImage*sizeImage))

    for i in range(image1.size[0] // 2):
        for j in range(image1.size[1] // 2):
            image1.putpixel((i, j), 0)

    image1.save("Trabalho2\Questao4\letraC\image1.png")

    mask = {}
    mask[0] = [0, 0, 0] 
    mask[1] = [0, 0, 0] 
    mask[2] = [0, 0, 0]  

    sizeKernel = 3
    openingImage = opening(image1, mask)

    # openingImage.show()
    openingImage.save("Trabalho2\Questao4\letraC\imageResult.png")

    diffImage = Image.new("1", (sizeImage, sizeImage))
    for i in range(image1.size[0]):
        for j in range(image1.size[1]):
            diff = image1.getpixel((i, j)) - openingImage.getpixel((i, j))
            diffImage.putpixel((i, j), diff)
    
    diffImage.save("Trabalho2\Questao4\letraC\diffImage.png")

    proveDiff = Image.new("1", (sizeImage, sizeImage))
    for i in range(image1.size[0]):
        for j in range(image1.size[1]):
            diff = diffImage.getpixel((i, j)) + openingImage.getpixel((i, j))
            proveDiff.putpixel((i, j), diff)
    
    proveDiff.save("Trabalho2\Questao4\letraC\proveDiff.png")
