import operator as op
from typing import Callable

from api import file_reader, parse

def concat(a: int, b: int):
	return int(str(a) + str(b))

def is_line_valid(line: list[int], wished_result: int, operators: list[Callable[[int, int], int]]):
	cur_results = {line[0]}
	for num in line[1:]:
		cur_results = {
			ope(cur_result, num)
			for cur_result in cur_results
			for ope in operators
		}
	return wished_result in cur_results

def get_input():
	num_pairs_lines = file_reader.get_lines('2024/07Example', parse.ints)
	results = [line[0] for line in num_pairs_lines]
	num_pairs = [list(line[1:]) for line in num_pairs_lines]
	return results, num_pairs

def test_first_star():
	results, num_pairs = get_input()
	result = 0
	for idx, num_pairs_line in enumerate(num_pairs):
		if is_line_valid(num_pairs_line, results[idx], [op.add, op.mul]):
			result += results[idx]
	assert 3749 == result

def test_second_star():
	results, num_pairs = get_input()
	result = 0
	for idx, num_pairs_line in enumerate(num_pairs):
		if is_line_valid(num_pairs_line, results[idx], [op.add, op.mul, concat]):
			result += results[idx]
	assert 11387 == result