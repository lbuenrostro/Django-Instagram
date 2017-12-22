from PIL import Image, ImageFilter
from resizeimage import resizeimage


def broken_glass(path):
    glass = Image.open('/static/insta/images/brokenglass.jpg').convert('RGB')

    image = Image.open(
        '/home/basecamp/Projects/Daily_Exercise/December/Django-insta/insta/static/insta/images/Bowling.png'
    ).convert('RGB')
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
        # avg = (r + g + b) // 3
        new_data.append((r, g, 50))

    new_img = Image.new('RGB', (w, h))
    new_img.putdata(new_data)
    new_img = resizeimage.resize_cover(new_img, [800, 800], validate=False)

    finalimage = Image.blend(new_img, glass, .3)
    finalimage.show()
