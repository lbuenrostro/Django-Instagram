from PIL import Image, ImageFilter
from resizeimage import resizeimage


def broken_glass(path):
    glass = Image.open(
        '/home/basecamp/Projects/Daily_Exercise/December/Django-insta/insta/static/insta/images/brokenglass.jpg'
    ).convert('RGB')

    image = Image.open(path).convert('RGB')
    w, h = image.size
    s = min([w, h])
    box = ((w - s) // 2, (h - s) // 2, (s + w) // 2, (s + h) // 2)
    image = image.crop(box=box)

    image = resizeimage.resize_cover(image, [800, 800], validate=False)
    image = image.convert('RGB')

    # get the new size
    w, h = image.size
    pixel_data = list(image.getdata())

    new_data = []
    for t in pixel_data:
        r, g, b = t
        new_data.append((r, g, 50))

    image = Image.new('RGB', (w, h))
    image.putdata(new_data)
    image = resizeimage.resize_cover(image, [800, 800], validate=False)

    finalimage = Image.blend(image, glass, .3)
    finalimage.save(path)
    return True


#############################################################################################
def make_grey(t):
    r, g, b = t
    grey = (r + g + b) // 3
    return (grey, grey, grey)


def convert_grayscale(path):
    image = Image.open(path).convert('RGB')

    # Get size
    width, height = image.size

    # get pixels
    pixels = image.getdata()

    # make the pixels all grey (average of r, g, b values)
    grey_pixels = list(map(make_grey, pixels))

    # create new image
    image = Image.new('RGB', (width, height))

    # put data in image
    image.putdata(grey_pixels)

    # save image to existing path
    image.save(path)

    return True


#############################################################################################
def rain_fall(path):
    rain = Image.open(
        '/home/basecamp/Projects/Daily_Exercise/December/Django-insta/insta/static/insta/images/rainfall.jpg'
    ).convert('RGB')

    image = Image.open(path).convert('RGB')
    w, h = image.size
    s = min([w, h])
    box = ((w - s) // 2, (h - s) // 2, (s + w) // 2, (s + h) // 2)
    image = image.crop(box=box)

    image = resizeimage.resize_cover(image, [800, 800], validate=False)
    image = image.convert('RGB')

    # get the new size
    w, h = image.size
    pixel_data = list(image.getdata())

    new_data = []
    for t in pixel_data:
        r, g, b = t
        new_data.append((r, g, 50))

    image = Image.new('RGB', (w, h))
    image.putdata(new_data)
    image = resizeimage.resize_cover(image, [800, 800], validate=False)

    finalimage = Image.blend(image, rain, .3)
    finalimage.save(path)
    return True


def main():
    image = Image.open(
        '/home/basecamp/Projects/Daily_Exercise/December/Django-insta/insta/static/insta/images/Bowling.png'
    ).convert('RGB')
    grey = convert_grayscale(image)
    grey.show()


if __name__ == '__main__':
    main()