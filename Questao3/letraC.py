from PIL import Image

import sys        
sys.path.append('D:\Programming\PDI\Trabalho2')
from AuxFunctions.diffTuple import diffTuple
from Questao3.letraA import convertToBinary

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
                if pixel1 == 255:
                    pixel1 = 1
                if pixel2 == 255:
                    pixel2 = 1
                    
                if pixel1 == 0 and pixel2 == 1:
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
    image1 = Image.open("Trabalho2\Questao3\image1.png")
    image2 = Image.open("Trabalho2\Questao3\image2.png")

    image1 = convertToBinary(image1)
    image2 = convertToBinary(image2)

    imageResult = diff(image1, image2)
    imageResult.save("Trabalho2\Questao3\letraC\imageResult.png")