from PIL import Image, ImageDraw
import random as rnd




#draw.ellipse((10,10,300,300), fill="red", outline="red")


for i in range(500):
	x1 = rnd.randint(0,300)
	y1 = rnd.randint(0,300)

	x2 = rnd.randint(0,300)
	y2 = rnd.randint(0,300)

	x3 = rnd.randint(0,300)
	y3 = rnd.randint(0,300)
	r = rnd.randint(0, 254)
	g = rnd.randint(0, 254)
	b = rnd.randint(0, 254)
	image = Image.new("RGBA", (320, 320), (0,0,0,0))
	draw = ImageDraw.Draw(image)
	draw.polygon([(x1, y1), (x2, y2), (x3, y3)], fill=(r, g, b))
	del draw
	image.save("./polygons/img{0}.png".format(i), "PNG")
	del image
