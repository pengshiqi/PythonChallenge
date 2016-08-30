content = open('evil2.gfx').read()

[open("12_%d.jpg" %i, "w").write(content[i::5]) for i in range(5)]