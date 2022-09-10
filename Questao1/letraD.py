from math import sqrt
from PIL import Image
from letraA import sumOfProducts

def applyLinearFilter(image, mask):
    lines = image.size[0]
    columns = image.size[1]
    newImage = Image.new(image.mode, (lines, columns))

    for i in range(1, lines - 1):
        for j in range(1, columns - 1):
            result = sumOfProducts(image, i, j, mask)
            newImage.putpixel((i, j), int(result))

    return newImage

def differenceBetween(image1, image2):
    lines = image1.size[0]
    columns = image1.size[1]
    newImage = Image.new(image1.mode, (lines, columns), color = 'white')
    for i in range(lines):
        for j in range(columns):
            pixel1 = image1.getpixel((i, j))
            pixel2 = image2.getpixel((i, j))
            newImage.putpixel((i, j), abs(pixel1 - pixel2))

    return newImage

def gradient(image1, image2):
    lines = image1.size[0]
    columns = image1.size[1]
    newImage = Image.new(image1.mode, (lines, columns), color = 'white')
    for i in range(lines):
        for j in range(columns):
            pixel1 = image1.getpixel((i, j))
            pixel2 = image2.getpixel((i, j))
            newImage.putpixel((i, j), int(sqrt(pow(pixel1, 2) + pow(pixel2, 2))))

    return newImage

if __name__ == '__main__':
    lenaImage = Image.open('Trabalho2\\lena_gray.bmp')
    pixelsLenaImage = lenaImage.load()

    sobelVerticalMask = {}
    sobelVerticalMask[0] = [-1, -2, -1] 
    sobelVerticalMask[1] = [0, 0, 0] 
    sobelVerticalMask[2] = [1, 2, 1]  

    sobelHorizontalMask = {}
    sobelHorizontalMask[0] = [-1, 0, 1] 
    sobelHorizontalMask[1] = [-2, 0, 2] 
    sobelHorizontalMask[2] = [-1, 0, 1] 

    prewittVerticalMask = {}
    prewittVerticalMask[0] = [-1, -1, -1] 
    prewittVerticalMask[1] = [0, 0, 0] 
    prewittVerticalMask[2] = [1, 1, 1]  

    prewittHorizontalMask = {}
    prewittHorizontalMask[0] = [-1, 0, 1] 
    prewittHorizontalMask[1] = [-1, 0, 1] 
    prewittHorizontalMask[2] = [-1, 0, 1] 

    sobelHorizontalImage = applyLinearFilter(lenaImage, sobelHorizontalMask)
    sobelHorizontalImage.save('Trabalho2\\Questao1\\Sobel-D\\lena_gray_horizontal_sobel.bmp')

    sobelVerticalImage = applyLinearFilter(lenaImage, sobelVerticalMask)
    sobelVerticalImage.save('Trabalho2\\Questao1\\Sobel-D\\lena_gray_vertical_sobel.bmp')

    prewittHorizontalImage = applyLinearFilter(lenaImage, prewittHorizontalMask)
    prewittHorizontalImage.save('Trabalho2\\Questao1\\prewitt-D\\lena_gray_horizontal_prewitt.bmp')

    prewittVerticalImage = applyLinearFilter(lenaImage, prewittVerticalMask)
    prewittVerticalImage.save('Trabalho2\\Questao1\\prewitt-D\\lena_gray_vertical_prewitt.bmp')

    differenceBetweenTwoImages = differenceBetween(sobelHorizontalImage, prewittHorizontalImage)
    differenceBetweenTwoImages.save('Trabalho2\\Questao1\\SobelAndPrewittDiff\\verticalDifferenceBetweenTwoImages.bmp')

    differenceBetweenTwoImages = differenceBetween(sobelVerticalImage, prewittVerticalImage)
    differenceBetweenTwoImages.save('Trabalho2\\Questao1\\SobelAndPrewittDiff\\horizontalDifferenceBetweenTwoImages.bmp')

    gradientImage = gradient(sobelHorizontalImage, sobelVerticalImage)
    gradientImage.save('Trabalho2\\Questao1\\Sobel-D\\lena_gray_gradient_sobel.bmp')

    gradientImage = gradient(prewittHorizontalImage, prewittVerticalImage)
    gradientImage.save('Trabalho2\\Questao1\\prewitt-D\\lena_gray_gradient_prewitt.bmp')