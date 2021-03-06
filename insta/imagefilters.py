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
    image = image.convert('RGB')

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
def rain_fall(path, side=800):
    rain = Image.open(
        '/home/basecamp/Projects/Daily_Exercise/December/Django-insta/insta/static/insta/images/rainfall.jpg'
    ).convert('RGB')
    rain = resizeimage.resize_cover(rain, [side, side], validate=False)
    rain = rain.convert('RGB').quantize(64).convert('RGB')

    image = Image.open(path).convert('RGB')
    w, h = image.size
    s = min([w, h])
    box = ((w - s) // 2, (h - s) // 2, (s + w) // 2, (s + h) // 2)
    image = image.crop(box=box)

    image = resizeimage.resize_cover(image, [side, side], validate=False)
    image = image.convert('RGB').quantize(255).convert('RGB')

    # get the new size
    w, h = image.size
    pixel_data = list(image.getdata())

    new_data = []
    n = len(pixel_data)
    for i in range(n):
        t = pixel_data[i]
        r, g, b = t
        new_data.append((max(0, int(r - 255 * (i**2 / n**2))), max(
            0, int(r - 255 * (i**2 / n**2))), b))

    image = Image.new('RGB', (w, h))
    image.putdata(new_data)
    image = resizeimage.resize_cover(image, [side, side], validate=False)
    image = image.convert('RGB')

    finalimage = Image.blend(image, rain, .4)
    finalimage.save(path)
    return True


#############################################################################################
def fire_all(path, side=800):
    fire = Image.open(
        '/home/basecamp/Projects/Daily_Exercise/December/Django-insta/insta/static/insta/images/fire.jpg'
    ).convert('RGB')
    fire = resizeimage.resize_cover(fire, [side, side], validate=False)
    fire = fire.convert('RGB').quantize(64).convert('RGB')

    image = Image.open(path).convert('RGB')
    w, h = image.size
    s = min([w, h])
    box = ((w - s) // 2, (h - s) // 2, (s + w) // 2, (s + h) // 2)
    image = image.crop(box=box)

    image = resizeimage.resize_cover(image, [side, side], validate=False)
    image = image.convert('RGB').quantize(255).convert('RGB')

    # get the new size
    w, h = image.size
    pixel_data = list(image.getdata())

    new_data = []
    n = len(pixel_data)
    for i in range(n):
        t = pixel_data[i]
        r, g, b = t
        new_data.append((r, max(0, int(r - 255 * (i**2 / n**2))), max(
            0, int(b - 255 * (i**2 / n**2)))))

    image = Image.new('RGB', (w, h))
    image.putdata(new_data)
    image = resizeimage.resize_cover(image, [side, side], validate=False)
    image = image.convert('RGB')

    finalimage = Image.blend(image, fire, .4)
    finalimage.save(path)
    return True


def main():
    grey = rain_fall(
        '/home/basecamp/Projects/Daily_Exercise/December/Django-insta/insta/static/insta/images/pug_zWBzUvm.jpg'
    )
    grey.show()


# path('filter/rain/<image_id>', views.rain_filter, name='rain'),

if __name__ == '__main__':
    main()