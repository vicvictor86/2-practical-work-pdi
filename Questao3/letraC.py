from PIL import Image
import numpy as np 

import sys        
sys.path.append('D:\Programming\PDI\Trabalho2')
from AuxFunctions.diffTuple import diffTuple

def diff(image1,image2):
    lines = image1.size[0]
    columns = image1.size[1]
    imageResult = Image.new(image1.mode, (lines, columns), color='white')
    
    for i in range(lines):
        for j in range(columns):
            result = 1
            pixel1 = image1.getpixel((i, j))
            pixel2 = image2.getpixel((i, j))

            if image1.mode == 'RGB' or image1.mode == 'RGBA':
                if diffTuple(pixel1, pixel2) == (0, 0, 0, 0):
                    result = (255, 255, 255, 255)
                else:
                    result = pixel1
            else:
                if pixel1 != pixel2:
                    result = 0
            imageResult.putpixel((i, j), result)
        
    return imageResult

def areDifferent(image1, image2):
    lines = image1.size[0]
    columns = image1.size[1]
    for i in range(lines):
        for j in range(columns):
            pixel1 = image1.getpixel((i, j))
            pixel2 = image2.getpixel((i, j))

            if image1.mode == 'RGB' or image1.mode == 'RGBA':
                if diffTuple(pixel1, pixel2) != (0, 0, 0, 0):
                    return True
            else:
                if pixel1 != pixel2:
                    return True
    return False

if __name__ == '__main__':
    sizeImage = 256
    image1 = Image.new("1", (sizeImage, sizeImage))
    image1.putdata(np.ones(sizeImage*sizeImage))

    image2 = Image.new("1", (sizeImage, sizeImage))
    image2.putdata(np.ones(sizeImage*sizeImage))

    for i in range(int(image1.size[0] / 2)):
        for j in range(int(image1.size[1] / 2)):
            image1.putpixel((i, j), 0)

    image1.save("Trabalho2\Questao3\letraC\image1.png")

    for i in range(int(image2.size[0] / 2)):
        for j in range(int(image2.size[1] / 2)):
            image2.putpixel((i, j), 0)

    for i in range(int(image1.size[0] / 2), int(image2.size[0])):
        for j in range(int(image1.size[1] / 2), int(image2.size[1])):
            image2.putpixel((i, j), 0)

    image2.save("Trabalho2\Questao3\letraC\image2.png")

    imageResult = diff(image1, image2)
    imageResult.show()
    imageResult.save("Trabalho2\Questao3\letraC\imageResult.png")