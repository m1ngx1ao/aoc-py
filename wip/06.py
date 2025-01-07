from api import file_reader

def vec_add(v: tuple[int, ...], w: tuple[int, ...]) -> tuple[int, ...]:
	return tuple(ve + we for ve, we in zip(v, w))

def vec_sub(v, w):
	return tuple(ve - we for ve, we in zip(v, w))

def vec_maxabs(v):
	return max(abs(ve) for ve in v)
d = {
	"O": (0, 0),
	"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1),
	"E": (1, 0), "W": (-1, 0), "N": (0, -1), "S": (0, 1),
	'>': (1, 0), '<': (-1, 0), '^': (0, -1), 'v': (0, 1)
}
O, E, W, N, S = [d[s] for s in 'OEWNS']
NE, SE, SW, NW = vec_add(N, E), vec_add(S, E), vec_add(S, W), vec_add(N, W)


lines = file_reader.get_lines('2024/06')
def get_start_things(laby):
	for idx_y, line in enumerate(laby):
		for idx_x, fach in enumerate(line):
			if fach in ('^', '>', '<', 'v'):
				return fach, (idx_x, idx_y)
	#will never become true
	return '>', (0, 0) 

def get_new_dir(dir: str) -> str:
	varie = '<^>v'
	return varie[(varie.index(dir) + 1) % len(varie)]

def get_result_of_laby(l: list[list[str]], obst_x, obst_y) -> bool:
	direction, pos = get_start_things(l)
	visited: set[tuple[tuple[int, int], str]] = set()
	x, y = pos
	width, height = len(l[0]), len(l)
	while ((x, y), direction) not in visited:
		visited.add(((x, y), direction))
		new_x, new_y = vec_add((x, y), d[direction])
		if 0 <= new_x < width and 0 <= new_y < height and (
			l[new_y][new_x] == '#' or (new_x, new_y) == (obst_x, obst_y)
		):
			direction = get_new_dir(direction)
		else:
			x, y = new_x, new_y
			if x < 0 or y < 0 or x >= width or y >= height:
				return False
	return True

def get_result():
	l = [
		list(line)
		for line in lines
	]
	result = 0
	for idx_y, line in enumerate(l):
		for idx_x, fach in enumerate(line):
			if fach == '.':
				if get_result_of_laby(l, idx_x, idx_y):
					result += 1
					if result % 50 == 0:
						print(result)
	return result