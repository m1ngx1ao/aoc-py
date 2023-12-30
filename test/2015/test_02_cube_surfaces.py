import itertools as it

from api import file_reader

def test_first():
	lines = file_reader.get_lines('2015/02')
	result = 0
	for line in lines:
		dims = [int(d) for d in line.split('x')]
		#a, b, c = dims
		#surfaces = [a * b, a * c, b * c]
		surfaces = [x * y for x, y in it.combinations(dims, 2)]
		result += min(surfaces) + 2 * sum(surfaces)
	assert 1606483 == result

#def test_second():
#	assert 0 == 1
