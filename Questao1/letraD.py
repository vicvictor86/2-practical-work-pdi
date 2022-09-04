from PIL import Image
from letraA import sumOfProducts
import cv2

if __name__ == '__main__':
    lenaImage = Image.open('Trabalho2\\lena_gray.bmp')
    pixelsLenaImage = lenaImage.load()

    mask = {}
    mask[0] = [1, 1, 1] 
    mask[1] = [1, 1, 1] 
    mask[2] = [1, 1, 1]  

    k = 2

    newImage = sobel(lenaImage, mask, k)
    newImage.save('Trabalho2\\Questao1\\unsharpMasking-B\\lena_gray_original.bmp')