from PIL import Image
import numpy as np 

def intersection(image1,image2):
    imageResult = Image.new(image1.mode, (image1.size[0], image1.size[1]))
    lines = image1.size[0]
    columns = image1.size[1]
    pixelsImage1 = image1.load()
    pixelsImage2 = image2.load()
    result = 0
    for i in range(lines):
        for j in range(columns):
            result = 1
            if pixelsImage1[i,j] == 0 and pixelsImage2[i,j] == 0:
                result = 0

            imageResult.putpixel((i, j), result)
    return imageResult

if __name__ == '__main__':
    sizeImage = 256
    image1 = Image.new("1", (sizeImage, sizeImage))
    image1.putdata(np.ones(sizeImage*sizeImage))

    image2 = Image.new("1", (sizeImage, sizeImage))
    image2.putdata(np.ones(sizeImage*sizeImage))

    for i in range(int(image1.size[0] / 2)):
        for j in range(int(image1.size[1] / 2)):
            image1.putpixel((i, j), 0)

    image1.save("Trabalho2\Questao3\letraB\image1.png")

    for i in range(int(image2.size[0] / 2)):
        for j in range(int(image2.size[1] / 2)):
            image2.putpixel((i, j), 0)

    for i in range(int(image1.size[0] / 2), int(image2.size[0])):
        for j in range(int(image1.size[1] / 2), int(image2.size[1])):
            image2.putpixel((i, j), 0)

    image2.save("Trabalho2\Questao3\letraB\image2.png")

    imageResult = intersection(image1, image2)
    imageResult.show()
    imageResult.save("Trabalho2\Questao3\letraB\imageResult.png")