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
O, E, W, N, S = [d[s] for s in 'OEWNS']
NE, SE, SW, NW = vec_add(N, E), vec_add(S, E), vec_add(S, W), vec_add(N, W)

#lines = file_reader.get_lines('2024/01')
#num_pairs = file_reader.get_lines('2024/03Example', parse.ints)
#num_pairs = file_reader.get_lines('2024/03', parse.ints)
