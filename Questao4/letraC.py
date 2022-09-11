from PIL import Image

from letraA import dilation
from letraB import erosion

import sys        
sys.path.append('D:\Programming\PDI\Trabalho2')
from AuxFunctions.diff import diff 

def opening(image, estructuralElement, structuralElementCenter=None):
    if structuralElementCenter is None:
        structuralElementCenter = len(estructuralElement) // 2

    erosionImage = erosion(image, estructuralElement, structuralElementCenter)
    erosionImage.save("Trabalho2\Questao4\letraC\erosionImage.png")

    openingImage = dilation(erosionImage, estructuralElement, structuralElementCenter)
    
    return openingImage

if __name__ == '__main__':
    image1 = Image.open("Trabalho2\Questao4\imageToOpening.png")

    estructuralElement = {}
    estructuralElement[0] = [0, 0, 0] 
    estructuralElement[1] = [0, 0, 0] 
    estructuralElement[2] = [0, 0, 0]  

    openingImage = opening(image1, estructuralElement)
    openingImage.save("Trabalho2\Questao4\letraC\imageResult.png")

    diffImage = diff(image1, openingImage)
    diffImage.save("Trabalho2\Questao4\letraC\diffImage.png")
