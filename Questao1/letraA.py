from PIL import Image

def proxPixel(image, i, ti,  j, tj):
    try:
        return image.getpixel((i + ti, j + tj))
    except IndexError:
        return 0

def sumOfProducts(image, xImage, yImage, mask):
    xInMask = 0
    result = 0
    rangeToSearch = len(mask) // 2

    for k in range(-rangeToSearch, rangeToSearch + 1):
        yInMask = 0
        for l in range(-rangeToSearch, rangeToSearch + 1):
            valueImage = proxPixel(image, xImage, k, yImage, l)

            result += valueImage * mask[xInMask][yInMask] 

            yInMask += 1
        xInMask += 1 
    return result

def applyLinearFilter(image, mask):
    lines = image.size[0]
    columns = image.size[1]
    newImage = Image.new(image.mode, (lines, columns))

    for i in range(lines):
        for j in range(columns):
            result = sumOfProducts(image, i, j, mask)
            newImage.putpixel((i, j), int(result))

    return newImage

def laplaciano(image, mask, c):
    lines = image.size[0]
    columns = image.size[1]
    newImage = Image.new(image.mode, (lines, columns))
    
    minimumValue = 0

    for i in range(lines):
        for j in range(columns):
            actualValuePixel = image.getpixel((i, j))

            if i == 0 and j == 0:
                minimumValue = actualValuePixel
            else:
                minimumValue = min(minimumValue, actualValuePixel)

            result = c * sumOfProducts(image, i, j, mask)
            
            newImage.putpixel((i, j), int(result))

    return newImage

def sharpImage(image, laplaciano):
    lines = image.size[0]
    columns = image.size[1]
    newImage = laplaciano.copy()

    for i in range(lines):
        for j in range(columns):
            #Correção da escala
            # newImage.putpixel((i, j), int(newImage.getpixel((i, j)) + minimumValue))

            newImage.putpixel((i, j), int(newImage.getpixel((i, j)) + image.getpixel((i, j))))
    
    return newImage

if __name__ == '__main__':
    lenaImage = Image.open('Trabalho2\\lena_gray.bmp')
    pixelsLenaImage = lenaImage.load()

    mask = {}
    mask[0] = [0, 1, 0] 
    mask[1] = [1, -4, 1] 
    mask[2] = [0, 1, 0]  

    c = -1

    laplacianoImage = laplaciano(lenaImage, mask, c)
    laplacianoImage.save('Trabalho2\\Questao1\\laplaciano-A\\lena_gray_laplaciano_result.bmp')

    sharpImage = sharpImage(lenaImage, laplacianoImage)
    sharpImage.save('Trabalho2\\Questao1\\laplaciano-A\\lena_gray_sharp_image.bmp')
