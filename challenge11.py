import Image

im = Image.open('cave.jpg', 'r')

w, h = im.size

even = Image.new(im.mode, (w / 2, h / 2))
odd = Image.new(im.mode, (w / 2, h / 2))

for x in xrange(w):
    for y in xrange(h):
        pixel = im.getpixel((x, y))
        if x % 2 or y % 2:
            odd.putpixel(((x - 1) / 2, y / 2) if x % 2 else (x / 2, (y - 1) / 2), pixel)
        else:
            even.putpixel((x / 2, y / 2), pixel)

odd.show()
even.show()