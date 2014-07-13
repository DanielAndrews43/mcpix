

filename = "map.txt"


def save_file(map_text):
	file = open(filename, 'w+')
	file.writelines(map_text)
	file.close()


def get_xcoord():
	while True:
		for i in range(0, 1001, 10):
			yield i


def get_ycoord():
	i = 0
	while True:
		yield i
		i += 10


def get_coords():
	y = get_ycoord()
	while True:
		y1 = next(y)
		y2 = y1 + 10

		x = get_xcoord()
		for i in range(100):
			x1 = next(x)
			x2 = x1 + 10

			yield [x1, y1, x2, y2]


def write_text():
	map_text = []

	_coords = get_coords()

	for i in range(10000):
		coords = next(_coords)
		coord_text = (str(coords[0]) + ", " + str(coords[1]) + ", " + str(coords[2]) + ", " + str(coords[3]))

		id = str(coords[0]).zfill(4) + str(coords[1]).zfill(4) + str(coords[2]).zfill(4) + str(coords[3]).zfill(4)

		text = '<area onmouseover="d(this)" onmouseout="e(this)" shape="rect" coord="' + coord_text + '" ' + \
			'href="/buy.php?id="' + id + '" title="Buy these pixels!"\n'

		map_text.append(text)
	save_file(map_text)


write_text()


