from PIL import Image

import sys

sys.path.append('D:\Programming\PDI\Trabalho2')
from Questao3.letraA import convertToBinary
from AuxFunctions.diff import diff        

if __name__ == '__main__':
    image1 = Image.open("Trabalho2\Questao3\image1.png")
    image2 = Image.open("Trabalho2\Questao3\image2.png")

    image1 = convertToBinary(image1)
    image2 = convertToBinary(image2)

    imageResult = diff(image1, image2)
    imageResult.save("Trabalho2\Questao3\letraC\imageResult.png")