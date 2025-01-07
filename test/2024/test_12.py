from api import file_reader, Grid, vec

d = {
	"O": (0, 0),
	"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1),
	"E": (1, 0), "W": (-1, 0), "N": (0, -1), "S": (0, 1),
	'>': (1, 0), '<': (-1, 0), '^': (0, -1), 'v': (0, 1)
}
O, E, W, N, S = [d[s] for s in 'OEWNS']
NE, SE, SW, NW = vec.add(N, E), vec.add(S, E), vec.add(S, W), vec.add(N, W)


def get_grid_and_loc():
	lines = file_reader.get_lines('2024/12')
	g = Grid.from_lines(lines)
	return g, g.size()

def is_neighbor(a: tuple[int, int], b: tuple[int, int]) -> bool:
	for v in [d[s] for s in 'EWNS']:
		if vec.add(a, v) == b:
			return True
	return False

def get_neighbors(a: tuple[int, int]) -> list[tuple[int, int]]:
	result = []
	for v in [d[s] for s in 'EWNS']:
		result.append(vec.add(a, v))
	return result

def get_region(start: tuple[int, int], grid: Grid, size: tuple[int, int]) -> set[tuple[int, int]]:
	width, height = size
	result = set()
	result.add(start)
	todo = set()
	todo.add(start)
	seen = set()
	while len(todo) > 0:
		current = todo.pop()
		if current not in seen:
			seen.add(current)
			neighbors = get_neighbors(current)
			for n in neighbors:
				n_x, n_y = n
				# in grid?
				if 0 <= n_x < width and 0 <= n_y < height:
					# same char?
					if grid[n] == grid[current]:
						todo.add(n)
						result.add(n)
	return result

def get_regions(g: Grid, size: tuple[int, int]) -> list[set[tuple[int, int]]]:
	result = []
	already_in_region = set()
	for coor in g.keys():
		if coor not in already_in_region:
			region = get_region(coor, g, size)
			result.append(region)
			already_in_region.update(region)
	return result


def test_first_star():
	grid, size = get_grid_and_loc()
	regions = get_regions(grid, size)
	result = 0
	for region in regions:
		perimeter = 0
		for c in region:
			for n in get_neighbors(c):
				if n not in region:
					perimeter += 1
		result += len(region) * perimeter
	assert 1402544 == result

def dd(a: tuple[int, int]):
	result = []
	for s in 'EWNS':
		result.append((s, vec.add(a, d[s])))
	return result

def test_second_star():
	grid, size = get_grid_and_loc()
	regions = get_regions(grid, size)
	result = 0
	for region in regions:
		perimeter = 0
		seen = set()
		for c in region:
			for string, new_coor in dd(c):
				if new_coor not in region:
					perimeter += 1
					seen.add((c, string))
					for dir in {'E': 'NS', 'W': 'NS', 'N': 'EW', 'S': 'EW'}[string]:
						if (vec.add(d[dir], c), string) in seen:
							perimeter -= 1
		result += len(region) * perimeter
	assert 862486 == result