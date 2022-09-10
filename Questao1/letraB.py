from PIL import Image
from letraA import sumOfProducts

#Borramento da imagem
def averageFilter(image, mask):
    blurredImage = Image.new(image.mode, (image.size[0], image.size[1]))
    lines = image.size[0]
    columns = image.size[1]

    for i in range(lines):
        for j in range(columns):
            sizeMask = len(mask)
            result = sumOfProducts(image, i, j, mask) / (sizeMask * sizeMask)
            blurredImage.putpixel((i, j), int(result))

    blurredImage.save('Trabalho2\\Questao1\\unsharpMasking-B\\lena_gray_blurred.bmp')

    return blurredImage

def unsharpMasking(image, mask, k):
    newImage = Image.new(image.mode, (image.size[0], image.size[1]))
    lines = image.size[0]
    columns = image.size[1]

    blurredMask = Image.new(image.mode, (image.size[0], image.size[1]))
    blurredImage = averageFilter(image, mask)

    #Subtração da imagem original com a imagem borrada
    for i in range(1, lines - 1):
        for j in range(1, columns - 1):
            blurredPixelValue = blurredImage.getpixel((i, j))
            originalPixelValue = image.getpixel((i, j))
            diffBlurredOriginal = originalPixelValue - blurredPixelValue

            blurredMask.putpixel((i, j), int(diffBlurredOriginal))

    blurredMask.save('Trabalho2\\Questao1\\unsharpMasking-B\\lena_gray_blurredMask.bmp')
    blurredMaskTemp = Image.new(image.mode, (image.size[0], image.size[1]))

    #Adição da imagem original com a máscara
    for i in range(1, lines - 1):
        for j in range(1, columns - 1):
            blurredMaskValue = k * blurredMask.getpixel((i, j))
            blurredMaskTemp.putpixel((i, j), int(blurredMaskValue))
            
            originalPixelValue = image.getpixel((i, j))
            sumBlurredOriginal = originalPixelValue + blurredMaskValue

            newImage.putpixel((i, j), int(sumBlurredOriginal))
    blurredMaskTemp.save('Trabalho2\\Questao1\\unsharpMasking-B\\lena_gray_blurredMaskTempk2.bmp')

    return newImage

if __name__ == '__main__':
    lenaImage = Image.open('Trabalho2\\lena_gray.bmp')

    mask = {}
    mask[0] = [1, 1, 1] 
    mask[1] = [1, 1, 1] 
    mask[2] = [1, 1, 1]  

    k = 1

    unsharpImage = unsharpMasking(lenaImage, mask, k)
    unsharpImage.save('Trabalho2\\Questao1\\unsharpMasking-B\\lena_gray_unsharp_masking.bmp')

    k = 2

    highBostImageK2 = unsharpMasking(lenaImage, mask, k)
    highBostImageK2.save('Trabalho2\\Questao1\\unsharpMasking-B\\lena_gray_high_boost_k_2.bmp')

    k = 4

    highBostImageK4 = unsharpMasking(lenaImage, mask, k)
    highBostImageK4.save('Trabalho2\\Questao1\\unsharpMasking-B\\lena_gray_high_boost_k_4.bmp')
