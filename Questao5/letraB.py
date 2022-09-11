from PIL import Image

import sys
sys.path.append('D:\Programming\PDI\Trabalho2')

from Questao5.letraA import isolateColor
from AuxFunctions.diff import diff

if __name__ == '__main__':
    black = (0, 0, 0, 255)

    image1 = Image.open("Trabalho2\Questao5\quadro.png")

    onlyBlackImage = isolateColor(image1, black)
    onlyBlackImage.save("Trabalho2\Questao5\letraB\onlyBlackImage.png")

    imageWithoutBlack = diff(image1, onlyBlackImage)
    imageWithoutBlack.save("Trabalho2\Questao5\letraB\imageWithoutBlack.png")
