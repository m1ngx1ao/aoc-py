import itertools as it

from api import file_reader, Grid, vec

def get_grid_and_loc():
	lines = file_reader.get_lines('2024/08')
	g = Grid.from_lines(lines)
	occurrences = g.occurrences()
	del occurrences['.']
	return occurrences, g.size()

def get_new_of_two(a: tuple[int, int], b: tuple[int, int], width: int, height: int):
	result = set()
	diff = vec.sub(b, a)
	p = b
	while 0 <= p[0] < width and 0 <= p[1] < height:
		result.add(p)
		p = vec.add(p, diff)
	return result

def get_result():
	occurrences, (width, height) = get_grid_and_loc()
	return len({
		tup
		for locations in occurrences.values()
		for a_loc, b_loc in it.permutations(locations, 2)
		for tup in get_new_of_two(a_loc, b_loc, width, height)
	})

def test_second_star():
	assert 962 == get_result()