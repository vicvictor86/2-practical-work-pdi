from PIL import Image

def diff(image1,image2):
    lines = image1.size[0]
    columns = image1.size[1]
    imageResult = Image.new(image1.mode, (lines, columns), color='white')
    
    for i in range(lines):
        for j in range(columns):
            result = 1
            pixel1 = image1.getpixel((i, j))
            pixel2 = image2.getpixel((i, j))

            if image1.mode == 'RGB' or image1.mode == 'RGBA':
                if pixel1 != (255, 255, 255, 255) and pixel2 == (255, 255, 255, 255):
                    result = pixel1
                else:
                    result = (255, 255, 255, 255)
            else:
                if pixel1 == 255:
                    pixel1 = 1
                if pixel2 == 255:
                    pixel2 = 1
                    
                if pixel1 == 0 and pixel2 == 1:
                    result = 0
            imageResult.putpixel((i, j), result)
        
    return imageResult