import itertools as it
from api import file_reader, parse

def get_nums():
	return file_reader.get_lines('2024/02', parse.ints)

def is_safe(line):
	diffs = {
		first - second
		for first, second in it.pairwise(line)
	}
	return diffs <= {1, 2, 3} or diffs <= {-1, -2, -3}

def is_safe_by_fn(line):
	pass

def is_safe_by_aggregate(line):
	pass

def test_first():
	lines = get_nums()
	safe_lines = [line for line in lines if is_safe(line)]
	#safe_lines = [line for line in lines if is_safe_by_fn(line)]
	#safe_lines = [line for line in lines if is_safe_by_aggregate(line)]
	assert 670 == len(safe_lines)

def test_second():
	assert 700 == sum(
		1 for line in get_nums()
		if any(is_safe(l) for l in it.combinations(line, len(line) - 1))
	)
