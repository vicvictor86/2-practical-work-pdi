from PIL import Image
from letraA import sumOfProducts

def averageFilter(image, mask):
    blurredImage = Image.new(image.mode, (image.size[0], image.size[1]))
    lines = image.size[0]
    columns = image.size[1]

    for i in range(lines):
        for j in range(columns):
            sizeMask = len(mask)
            result = sumOfProducts(image, i, j, mask) / (sizeMask * sizeMask)
            blurredImage.putpixel((i, j), int(result))

    return blurredImage

def unsharpMasking(image, mask, k):
    newImage = Image.new(image.mode, (image.size[0], image.size[1]))
    lines = image.size[0]
    columns = image.size[1]

    blurredMask = Image.new(image.mode, (image.size[0], image.size[1]))
    blurredImage = averageFilter(image, mask)

    for i in range(lines):
        for j in range(columns):
            blurredPixelValue = blurredImage.getpixel((i, j))
            originalPixelValue = image.getpixel((i, j))
            diffBlurredOriginal = originalPixelValue - blurredPixelValue

            blurredMask.putpixel((i, j), int(diffBlurredOriginal))

    for i in range(lines):
        for j in range(columns):
            blurredMaskValue = k * blurredMask.getpixel((i, j))
            originalPixelValue = image.getpixel((i, j))
            sumBlurredOriginal = originalPixelValue + blurredMaskValue

            newImage.putpixel((i, j), int(sumBlurredOriginal))

    return newImage

if __name__ == '__main__':
    lenaImage = Image.open('Trabalho2\\lena_gray.bmp')
    pixelsLenaImage = lenaImage.load()

    mask = {}
    mask[0] = [1, 1, 1] 
    mask[1] = [1, 1, 1] 
    mask[2] = [1, 1, 1]  

    k = 1

    unsharpImage = unsharpMasking(lenaImage, mask, k)
    unsharpImage.save('Trabalho2\\Questao1\\unsharpMasking-B\\lena_gray_unsharp_masking.bmp')

    k = 4

    highBostImage = unsharpMasking(lenaImage, mask, k)
    highBostImage.save('Trabalho2\\Questao1\\unsharpMasking-B\\lena_gray_high_boost.bmp')
