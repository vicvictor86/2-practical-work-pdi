from PIL import Image
import numpy as np 

from Questao4.letraA import dilation
from Questao4.letraB import erosion

def closing(image, kernel):
    dilatadedImage = dilation(image, kernel)
    dilatadedImage.save("Trabalho2\Questao4\letraD\dilatadedImage.png")

    closingImage = erosion(dilatadedImage, kernel)
    closingImage.save("Trabalho2\Questao4\letraD\closingImage.png")
    
    return closingImage

if __name__ == '__main__':
    sizeImage = 10
    image1 = Image.new("1", (sizeImage, sizeImage))
    image1.putdata(np.ones(sizeImage*sizeImage))

    for i in range(image1.size[0] // 2):
        for j in range(image1.size[1] // 2):
            image1.putpixel((i, j), 0)

    image1.save("Trabalho2\Questao4\letraD\image1.png")

    mask = {}
    mask[0] = [0, 0, 0] 
    mask[1] = [0, 0, 0] 
    mask[2] = [0, 0, 0]  

    sizeKernel = 3
    closingImage = closing(image1, mask)

    # closingImage.show()
    closingImage.save("Trabalho2\Questao4\letraD\imageResult.png")

    diffImage = Image.new("1", (sizeImage, sizeImage))
    for i in range(image1.size[0]):
        for j in range(image1.size[1]):
            diff = image1.getpixel((i, j)) - closingImage.getpixel((i, j))
            diffImage.putpixel((i, j), diff)
    
    diffImage.save("Trabalho2\Questao4\letraD\diffImage.png")

    proveDiff = Image.new("1", (sizeImage, sizeImage))
    for i in range(image1.size[0]):
        for j in range(image1.size[1]):
            diff = diffImage.getpixel((i, j)) + closingImage.getpixel((i, j))
            proveDiff.putpixel((i, j), diff)
    
    proveDiff.save("Trabalho2\Questao4\letraC\proveDiff.png")
