import math
import itertools as it
import re
from collections import defaultdict

from api import file_reader, parse

def vec_add(v, w):
	return tuple(ve + we for ve, we in zip(v, w))

def vec_sub(v, w):
	return tuple(ve - we for ve, we in zip(v, w))

def vec_maxabs(v):
	return max(abs(ve) for ve in v)

d = {
	"O": (0, 0),
	"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1),
	"E": (1, 0), "W": (-1, 0), "N": (0, -1), "S": (0, 1)
}

inp = ''.join(file_reader.get_lines('2024/03'))
segemente = inp.split('do()')
segmente = [s.split("don't()") for s in segemente]
result = 0
for s in segemente:
	segment = s.split("don't()")
	candidates = re.findall(r'mul\((\d+),(\d+)\)', segment[0])
	result += sum(
		int(first) * int(second)
		for first, second in candidates
	)
print(result)
#num_pairs = file_reader.get_lines('2024/03Example', parse.ints)
#num_pairs = file_reader.get_lines('2024/03', parse.ints)

#print(lines[0])
#27636   67663

#print(num_pairs[0])
#[27636, 67663]

#line = '21-61 red'
#[21, 61]
#print(parse.uints(line))