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

def laplaciano(image, mask, c):
    lines = image.size[0]
    columns = image.size[1]
    newImage = Image.new(image.mode, (lines, columns))

    # Percorre a imagem ignorando as bordas
    for i in range(1, lines - 1):
        for j in range(1, columns - 1):
            #Realiza a soma dos produtos com a máscara do filtro laplaciano
            result = c * sumOfProducts(image, i, j, mask)
            
            newImage.putpixel((i, j), int(result))

    return newImage

def sharpImage(image, laplaciano):
    lines = image.size[0]
    columns = image.size[1]
    newImage = Image.new(image.mode, (lines, columns))

    for i in range(1, lines - 1):
        for j in range(1, columns - 1):
            #Adição de imagem original com a imagem laplaciana
            newImage.putpixel((i, j), int(laplaciano.getpixel((i, j)) + image.getpixel((i, j))))
    
    return newImage

if __name__ == '__main__':
    lenaImage = Image.open('Trabalho2\\lena_gray.bmp')

    mask = {}
    mask[0] = [0, 1, 0] 
    mask[1] = [1, -4, 1] 
    mask[2] = [0, 1, 0]  

    c = -1

    laplacianoImage = laplaciano(lenaImage, mask, c)
    laplacianoImage.save('Trabalho2\\Questao1\\laplaciano-A\\lena_gray_laplaciano_result.bmp')

    sharpImage = sharpImage(lenaImage, laplacianoImage)
    sharpImage.save('Trabalho2\\Questao1\\laplaciano-A\\lena_gray_sharp_image.bmp')
