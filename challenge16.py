import Image

im = Image.open('mozart.gif')

print im.mode, im.size

# 找到第一个粉红色的点，并以此对齐
def straighten(line):
    i = 0
    while line[i] != 195:
        i += 1
    return line[i:] + line[:i]

for h in range(im.size[1]):
    line = [im.getpixel((w, h)) for w in range(im.size[0])]
    line = straighten(line)
    [im.putpixel((w, h), line[w]) for w in range(im.size[0])]

im.show()