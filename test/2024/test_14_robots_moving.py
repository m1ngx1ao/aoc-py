from api import file_reader, parse, vec

d = {
	"O": (0, 0),
	"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1),
	"E": (1, 0), "W": (-1, 0), "N": (0, -1), "S": (0, 1),
	'>': (1, 0), '<': (-1, 0), '^': (0, -1), 'v': (0, 1)
}

def test_first_star():
	robots_coors = file_reader.get_lines('2024/14', parse.ints)
	width = 101
	height = 103
	secs = 100
	center = ((width//2)-1, (height//2)-1)
	quadrant1 = [0, 0, center[0], center[1], 1]
	quadrant2 = [center[0] + 2, 0, width-1, center[1], 2]
	quadrant3 = [0, center[1] + 2, center[0], height-1, 3]
	quadrant4 = [center[0] + 2, center[1] + 2, width-1, height-1, 4]
	robots_pos = []
	dici = {1: 0, 2: 0, 3: 0, 4: 0}
	for robot_coor in robots_coors:
		start, move = robot_coor[:2], robot_coor[2:]
		endposx, endposy = vec.add(start, vec.mul(move, secs))
		robots_pos.append((endposx % width, endposy % height))
	for posx, posy in robots_pos:
		for q in [quadrant1, quadrant2, quadrant3, quadrant4]:
			if q[0] <= posx <= q[2] and q[1] <= posy <= q[3]:
				dici[q[4]] += 1
	result = 1
	for r in dici.values():
		result *= r
	assert 211773366 == result

import time
import itertools as it

from api import file_reader, parse, Grid, vec

robots_coors = file_reader.get_lines('2024/14', parse.ints)

width = 101
height = 103
#output = [
#	[' ' for _ in range(width)]
#	for _ in range(height)
#]
#for start in robots_coors:
#	sx, sy = start[:2]
#	output[sy][sx] = 'X'
#string_output = ''
#for line in output:
#	str_line = ''.join(line) + '\n'
#	string_output += str_line
#print(string_output)

starts = []
moves = []
for start in robots_coors:
	starts.append(start[:2])
	moves.append(start[2:])

d = {
	"O": (0, 0),
	"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1),
	"E": (1, 0), "W": (-1, 0), "N": (0, -1), "S": (0, 1),
	'>': (1, 0), '<': (-1, 0), '^': (0, -1), 'v': (0, 1)
}
dirs = 'NESW'

# secs for christmas tree: 7344
def second_star():
	for secs in range(1, 10000):
		new_pos = []
		for idx, start in enumerate(starts):
			move = moves[idx]
			x, y = vec.add(start, move)
			endposx, endposy = x % width, y % height
			new_pos.append((endposx, endposy))
		starts = new_pos
		positions = set(new_pos)
		robots_counter = 0
		for position in positions:
			robot_counter = 0
			for dir in dirs:
				if vec.add(position, d[dir]) in positions:
					robot_counter += 1
			if robot_counter >= 2:
				robots_counter += 1
		if robots_counter > len(starts) // 2:
			output = [
				[' ' for _ in range(width)]
				for _ in range(height)
			]
			for x, y in starts:
				output[y][x] = 'X'
			string_output = ''
			for line in output:
				str_line = ''.join(line) + '\n'
				string_output += str_line
			print(string_output)
			print('\n' + str(secs) + '\n\n')
		if secs % 100 == 0:
			print(secs)