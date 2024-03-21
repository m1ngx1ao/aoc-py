import math
from collections import defaultdict

from api import file_reader

def get_max_color(line: str) -> dict[str, int]:
	d = defaultdict(int)
	l = line.split(': ')
	for draw in l[1].split('; '):
		for partner in draw.split(', '):
			number, color = partner.split(' ')
			d[color] = max(d[color], int(number))
	return d

def test_first():
	lines = file_reader.get_lines('2023/02')
	result = 0
	for i, line in enumerate(lines):
		d = get_max_color(line)
		if d['red'] <= 12 and d['green'] <= 13 and d['blue'] <= 14:
			result += i + 1
	assert 2265 == result

def test_second():
	lines = file_reader.get_lines('2023/02')
	result = sum(
		math.prod(get_max_color(line).values())
		for line in lines
	)
	assert 64097 == result