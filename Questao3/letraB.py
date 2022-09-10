from PIL import Image

import sys        
sys.path.append('D:\Programming\PDI\Trabalho2')
from Questao3.letraA import convertToBinary

def intersection(image1,image2):
    imageResult = Image.new(image1.mode, (image1.size[0], image1.size[1]))
    lines = image1.size[0]
    columns = image1.size[1]
    
    result = 0
    for i in range(lines):
        for j in range(columns):
            result = 1
            if image1.getpixel((i, j)) == 0 and image2.getpixel((i, j)) == 0:
                result = 0

            imageResult.putpixel((i, j), result)
    return imageResult

if __name__ == '__main__':
    image1 = Image.open("Trabalho2\Questao3\image1.png")
    image2 = Image.open("Trabalho2\Questao3\image2.png")

    image1 = convertToBinary(image1)
    image2 = convertToBinary(image2)

    imageResult = intersection(image1, image2)
    imageResult.save("Trabalho2\Questao3\letraB\imageResult.png")