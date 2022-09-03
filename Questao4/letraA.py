from PIL import Image
import numpy as np 

# import sys        
# sys.path.append('D:\Programming\PDI\Trabalho2')
# from Questao3.letraA import intersection

def dilation(image, kernel):
    imageResult = Image.new("1", (image.size[0], image.size[1]))
    lines = image.size[0]
    columns = image.size[1]
    pixelsImage = image.load()
    result = 1
    for i in range(lines):
        for j in range(columns):
            result = 1
            for k in range(-sizeKernel, sizeKernel):
                for l in range(-sizeKernel, sizeKernel):
                    if (i+k) < lines and (j+l) < columns:
                        if pixelsImage[i+k, j+l] == 0 and kernel[k, l] == 0:
                            result = 0
                        imageResult.putpixel((i+k, j+l), result)
    return imageResult

sizeImage = 256
image1 = Image.new("1", (sizeImage, sizeImage))
image1.putdata(np.ones(sizeImage*sizeImage))

for i in range(int(image1.size[0] / 2)):
    for j in range(int(image1.size[1] / 2)):
        image1.putpixel((i, j), 0)

image1.save("Trabalho2\Questao4\letraA\image1.png")

sizeKernel = 3
dilationImage = dilation(image1, np.zeros((sizeKernel,sizeKernel)))

dilationImage.show()
dilationImage.save("Trabalho2\Questao4\letraA\imageResult.png")