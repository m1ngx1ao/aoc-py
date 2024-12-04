import math
import itertools as it
import re
from collections import defaultdict

from api import file_reader

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

#inp = ''.join(file_reader.get_lines('2024/04'))
lines = file_reader.get_lines('2024/04')
inp = [
	[
		idx
		for idx in line
	]
	for line in lines	
]

result = 0
for y in range(2, len(inp)):
	for idx in range(2, len(inp[0])):
		first = inp[y-2][idx-2]
		second = inp[y-1][idx-1]
		third = inp[y][idx]
		three_str = first + second + third
		if three_str in ('SAM', 'MAS'):
			first = inp[y-2][idx]
			second = inp[y-1][idx-1]
			third = inp[y][idx-2]
			three_str = first + second + third
			if three_str in ('SAM', 'MAS'):
				result+=1

print(result)