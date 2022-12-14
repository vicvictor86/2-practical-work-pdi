from PIL import Image

import sys        
sys.path.append('D:\Programming\PDI\Trabalho2')

from Questao4.letraA import dilation
from Questao4.letraB import erosion
from AuxFunctions.diff import diff 

def closing(image, estructuralElement, structuralElementCenter=None):
    if structuralElementCenter is None:
        structuralElementCenter = len(estructuralElement) // 2

    dilatadedImage = dilation(image, estructuralElement, structuralElementCenter)

    closingImage = erosion(dilatadedImage, estructuralElement, structuralElementCenter)
    
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

    diffImage = diff(closingImage, image1)
    diffImage.save("Trabalho2\Questao4\letraD\diffImage3x3.png")

    closingImage = closing(image1, estructuralElement5x5)
    closingImage.save("Trabalho2\Questao4\letraD\imageResult5x5.png")

    diffImage = diff(closingImage, image1)
    diffImage.save("Trabalho2\Questao4\letraD\diffImage5x5.png")