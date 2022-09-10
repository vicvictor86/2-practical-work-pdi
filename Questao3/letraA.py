from PIL import Image

def convertToBinary(image):
    lines = image.size[0]
    columns = image.size[1]
    newImage = Image.new("1", (lines, columns), color = 'white')

    for i in range(lines):
        for j in range(columns):
            pixel = image.getpixel((i, j))
            
            if pixel == 255:
                newImage.putpixel((i, j), 1)
            else:
                newImage.putpixel((i, j), 0)

    return newImage

def union(image1,image2):
    imageResult = Image.new(image1.mode, (image1.size[0], image1.size[1]))
    lines = image1.size[0]
    columns = image1.size[1]
    result = 0
    for i in range(lines):
        for j in range(columns):
            result = 1
            if image1.getpixel((i, j)) == 0 or image2.getpixel((i, j)) == 0:
                result = 0

            imageResult.putpixel((i, j), result)
    return imageResult
    
if __name__ == '__main__':
    image1 = Image.open("Trabalho2\Questao3\image1.png")
    image2 = Image.open("Trabalho2\Questao3\image2.png")

    image1 = convertToBinary(image1)
    image2 = convertToBinary(image2)

    imageResult = union(image1, image2)
    imageResult.save("Trabalho2\Questao3\letraA\imageResult.png")