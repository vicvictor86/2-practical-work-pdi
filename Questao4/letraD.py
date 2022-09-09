from PIL import Image

import sys        
sys.path.append('D:\Programming\PDI\Trabalho2')

from Questao4.letraA import dilation
from Questao4.letraB import erosion
from Questao3.letraC import diff

def closing(image, estructuralElement):
    dilatadedImage = dilation(image, estructuralElement)

    closingImage = erosion(dilatadedImage, estructuralElement)
    
    return closingImage

if __name__ == '__main__':
    image1 = Image.open("Trabalho2\Questao4\imageToClosing.png")

    estructuralElement3x3 = {}
    estructuralElement3x3[0] = [0, 0, 0] 
    estructuralElement3x3[1] = [0, 0, 0] 
    estructuralElement3x3[2] = [0, 0, 0]  

    estructuralElement5x5 = {}
    estructuralElement5x5[0] = [0, 0, 0, 0, 0]
    estructuralElement5x5[1] = [0, 0, 0, 0, 0]
    estructuralElement5x5[2] = [0, 0, 0, 0, 0]
    estructuralElement5x5[3] = [0, 0, 0, 0, 0]
    estructuralElement5x5[4] = [0, 0, 0, 0, 0]

    closingImage = closing(image1, estructuralElement3x3)
    closingImage.save("Trabalho2\Questao4\letraD\imageResult3x3.png")

    diffImage = diff(image1, closingImage)
    diffImage.save("Trabalho2\Questao4\letraD\diffImage3x3.png")

    closingImage = closing(image1, estructuralElement5x5)
    closingImage.save("Trabalho2\Questao4\letraD\imageResult5x5.png")

    diffImage = diff(image1, closingImage)
    diffImage.save("Trabalho2\Questao4\letraD\diffImage5x5.png")