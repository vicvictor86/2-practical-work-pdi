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
    newImage = Image.new(image.mode, (image.size[0], image.size[1]))
    lines = image.size[0]
    columns = image.size[1]

    for i in range(lines):
        for j in range(columns):
            result = c * sumOfProducts(image, i, j, mask)
            newImage.putpixel((i, j), int(result))

    return newImage

if __name__ == '__main__':
    lenaImage = Image.open('Trabalho2\\lena_gray.bmp')
    pixelsLenaImage = lenaImage.load()

    mask = {}
    mask[0] = [0, 1, 0] 
    mask[1] = [1, -4, 1] 
    mask[2] = [0, 1, 0]  

    c = 1

    newImage = laplaciano(lenaImage, mask, c)
    newImage.save('Trabalho2\\Questao1\\laplaciano-A\\lena_gray_filtered.bmp')
