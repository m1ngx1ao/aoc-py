import math
import itertools as it
from collections import defaultdict

from aoc import file_reader

lines = file_reader.get_lines('2023/01')
result = 0
for i, l in enumerate(lines):
	result += 1
print(result)