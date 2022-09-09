from PIL import Image
import numpy as np 

from letraA import dilation
from letraB import erosion

import sys        
sys.path.append('D:\Programming\PDI\Trabalho2')
from Questao3.letraC import diff

def opening(image, kernel):
    erosionImage = erosion(image, kernel)
    erosionImage.save("Trabalho2\Questao4\letraC\erosionImage.png")

    openingImage = dilation(erosionImage, kernel)
    openingImage.save("Trabalho2\Questao4\letraC\openingImage.png")
    
    return openingImage

if __name__ == '__main__':
    image1 = Image.open("Trabalho2\Questao4\imageToOpening.png")

    mask = {}
    mask[0] = [0, 0, 0] 
    mask[1] = [0, 0, 0] 
    mask[2] = [0, 0, 0]  

    openingImage = opening(image1, mask)
    openingImage.save("Trabalho2\Questao4\letraC\imageResult.png")

    diffImage = diff(image1, openingImage)
    diffImage.save("Trabalho2\Questao4\letraC\diffImage.png")
