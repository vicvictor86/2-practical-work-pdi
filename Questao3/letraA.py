from PIL import Image
import numpy as np 

def createImage(sizeImage, start, end):
    newImage = Image.new("1", (sizeImage, sizeImage))
    newImage.putdata(np.ones(sizeImage*sizeImage))

    for i in range(start, end):
        for j in range(start, end):
            newImage.putpixel((i, j), 0)
    

sizeImage = 256
image1 = Image.new("1", (sizeImage, sizeImage))
image1.putdata(np.ones(sizeImage*sizeImage))

image2 = Image.new("1", (sizeImage, sizeImage))
image2.putdata(np.ones(sizeImage*sizeImage))

for i in range(int(image1.size[0] / 2)):
    for j in range(int(image1.size[1] / 2)):
        image1.putpixel((i, j), 0)

image1.save("Trabalho2\Questao3\letraA\image1.png")

for i in range(int(image1.size[0] / 2), int(image2.size[0])):
    for j in range(int(image1.size[1] / 2), int(image2.size[1])):
        image2.putpixel((i, j), 0)

image2.save("Trabalho2\Questao3\letraA\image2.png")

def union(image1,image2):
    imageResult = Image.new("1", (image1.size[0], image1.size[1]))
    lines = image1.size[0]
    columns = image1.size[1]
    pixelsImage1 = image1.load()
    pixelsImage2 = image2.load()
    result = 0
    for i in range(lines):
        for j in range(columns):
            result = 1
            if pixelsImage1[i,j] == 0 or pixelsImage2[i,j] == 0:
                result = 0

            imageResult.putpixel((i, j), result)
    return imageResult

imageResult = union(image1, image2)
imageResult.show()
imageResult.save("Trabalho2\Questao3\letraA\imageResult.png")