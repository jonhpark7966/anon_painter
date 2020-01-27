from PIL import Image, ImageDraw, ImageFilter





mask = Image.new("L", (100,100), 0)
draw = ImageDraw.Draw(mask)
draw.polygon((0, 0, 100,0, 50,100, 0,100), fill=255)
mask.save("test.jpg")
