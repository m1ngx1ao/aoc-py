import re
from api import file_reader

def get_line():
	return ''.join(file_reader.get_lines('2024/03'))

def get_result(candidates):
	return sum(
		int(first) * int(second)
		for first, second in candidates
	)

def test_first():
	assert 173529487 == get_result(re.findall(r'mul\((\d+),(\d+)\)', get_line()))

def test_second():
	result = 0
	for s in get_line().split('do()'):
		segment = s.split("don't()")
		result += get_result(re.findall(r'mul\((\d+),(\d+)\)', segment[0]))
	assert 99532691 == result