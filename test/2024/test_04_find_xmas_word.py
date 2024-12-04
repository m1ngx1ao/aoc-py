from collections import defaultdict

from api import file_reader

def vec_add(*vs):
	return tuple(sum(c) for c in zip(*vs))

directions = {
	"O": (0, 0),
	"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1),
	"E": (1, 0), "W": (-1, 0), "N": (0, -1), "S": (0, 1)
}
O, E, W, N, S = [directions[s] for s in 'OEWNS']
NE, SE, SW, NW = vec_add(N, E), vec_add(S, E), vec_add(S, W), vec_add(N, W)

def get_grid():
	d = defaultdict(str)
	for idx_y, line in enumerate(file_reader.get_lines('2024/04')):
		for idx_x, fach in enumerate(line):
			d[idx_x, idx_y] = fach
	return d

def get_word(g, c, d, steps):
	result = ''
	for _ in range(steps):
		result += g[c]
		c = vec_add(c, d)
	return result

def test_first():
	g = get_grid()
	keys = set(g.keys())
	assert 2447 == sum(
		get_word(g, coor, (x, y), 4) == 'XMAS'
		for coor in keys
		for y in range(-1, 2)
		for x in range(-1, 2)
	)

def test_second():
	g = get_grid()
	keys = set(g.keys())
	result = sum(
		{
			get_word(g, coor, SE, 3),
			get_word(g, vec_add(coor, S, S), NE, 3)
		} <= {'MAS', 'SAM'}
		for coor in keys
	)
	assert 1868 == result