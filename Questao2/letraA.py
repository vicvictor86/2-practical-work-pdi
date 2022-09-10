from PIL import Image
from statistics import median

import sys        
sys.path.append('D:/Programming/PDI/Trabalho2')
from Questao1.letraA import sumOfProducts, proxPixel

def weightedAverage(image, mask, weight):
    lines = image.size[0]
    columns = image.size[1]
    newImage = Image.new(image.mode, (lines, columns))

    for i in range(lines):
        for j in range(columns):
            result = sumOfProducts(image, i, j, mask) / weight
            newImage.putpixel((i, j), int(result))

    return newImage

def medianFilter(image, sizeMedianMask):
    lines = image.size[0]
    columns = image.size[1]
    newImage = Image.new(image.mode, (lines, columns))

    rangeToSearch = sizeMedianMask // 2

    for i in range(lines):
        for j in range(columns):
            medianList = []
            for k in range(-rangeToSearch, rangeToSearch + 1):
                for l in range(-rangeToSearch, rangeToSearch + 1):
                    valueImage = proxPixel(image, i, k, j, l)

                    medianList.append(valueImage)

            medianValue = median(medianList)
            newImage.putpixel((i, j), int(medianValue))

    return newImage

if __name__ == '__main__':
    lenaImage = Image.open('Trabalho2\\lena_ruido.bmp')

    mask1 = {}
    mask1[0] = [0, 1, 0] 
    mask1[1] = [1, 1, 1] 
    mask1[2] = [0, 1, 0]  
    weight1 = 5

    mask2 = {}
    mask2[0] = [1, 1, 1] 
    mask2[1] = [1, 1, 1] 
    mask2[2] = [1, 1, 1]  
    weight2 = 9

    mask3 = {}
    mask3[0] = [1, 3, 1] 
    mask3[1] = [3, 16, 3] 
    mask3[2] = [1, 3, 1]  
    weight3 = 32

    mask4 = {}
    mask4[0] = [0, 1, 0] 
    mask4[1] = [1, 4, 1] 
    mask4[2] = [0, 1, 0]  
    weight4 = 8

    newImage1 = weightedAverage(lenaImage, mask1, weight1)
    newImage1.save('Trabalho2\\Questao2\\letraA\\lena_gray_filtered_1.bmp')

    newImage2 = weightedAverage(lenaImage, mask2, weight2)
    newImage2.save('Trabalho2\\Questao2\\letraA\\lena_gray_filtered_2.bmp')

    newImage3 = weightedAverage(lenaImage, mask3, weight3)
    newImage3.save('Trabalho2\\Questao2\\letraA\\lena_gray_filtered_3.bmp')

    newImage4 = weightedAverage(lenaImage, mask4, weight4)
    newImage4.save('Trabalho2\\Questao2\\letraA\\lena_gray_filtered_4.bmp')

    sizeMedianMask = 3
    newImage5 = medianFilter(lenaImage, sizeMedianMask)
    newImage5.save('Trabalho2\\Questao2\\letraA\\lena_gray_filtered_5.bmp')
