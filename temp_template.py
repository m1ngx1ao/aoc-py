import math
import itertools as it
import re
import heapq
from collections import defaultdict

from api import file_reader, parse, Grid, vec

d = {
	"O": (0, 0),
	"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1),
	"E": (1, 0), "W": (-1, 0), "N": (0, -1), "S": (0, 1),
	'>': (1, 0), '<': (-1, 0), '^': (0, -1), 'v': (0, 1)
}
O, E, W, N, S = [d[s] for s in 'OEWNS']
NE, SE, SW, NW = vec.add(N, E), vec.add(S, E), vec.add(S, W), vec.add(N, W)

#output = [
#	[' ' for _ in range(width)]
#	for _ in range(height)
#]

def get_grid_and_loc():
	lines = file_reader.get_lines('2024/09')
	g = Grid.from_lines(lines)
	occurrences = g.occurrences()
	del occurrences['.']
	return occurrences, g.size()


#lines = file_reader.get_lines('2024/15Example')
#lines = file_reader.get_lines('2024/15')
num_pairs = file_reader.get_lines('2024/15', parse.ints)
#num_pairs = file_reader.get_lines('2024/15Example', parse.ints)
