from api import file_reader, Grid, vec

d = {
	"O": (0, 0),
	"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1),
	"E": (1, 0), "W": (-1, 0), "N": (0, -1), "S": (0, 1),
	'>': (1, 0), '<': (-1, 0), '^': (0, -1), 'v': (0, 1)
}

# :wall
# O: box
# @: robot start
# .: nothing

def get_grid_and_loc():
	lines = file_reader.get_lines('2024/15')
	new_lines = [
		line.replace('.', '..').replace('#', '##').replace('O', '[]').replace('@', '@.')
		for line in lines[0:-1]
	]
	g = Grid.from_lines(new_lines)
	occurrences = g.occurrences()
	moves = lines[-1]
	return occurrences['@'].pop(), moves, g.size(), g

def print_grid(grid, i, robot_pos, size, order_str):
	print('moves: ' + str(i) + '\n' + 'robot position: ' + str(robot_pos) + '\n' + 'robot direction: ' + order_str + '\n')
	output = [
		[' ' for _ in range(size[0])]
		for _ in range(size[1])
	]
	for (x, y), char in grid.items():
		output[y][x] = char
	string_output = ''
	for line in output:
		str_line = ''.join(line) + '\n'
		string_output += str_line
	print(string_output)
	#input()


def make_moves():
	robot_pos, orders_str, (width, height), grid = get_grid_and_loc()
	for i, order_str in enumerate(orders_str):
		order_dir = d[order_str]
		#print_grid(grid, i, robot_pos, (width, height), order_str)
		next_robot_pos = vec.add(robot_pos, order_dir)
		next_robot_pos_x, next_robot_pos_y = next_robot_pos
		obstacle = grid[next_robot_pos]
		if 0 <= next_robot_pos_x < width and 0 <= next_robot_pos_y < height:
			if obstacle == '.':
				grid[robot_pos], grid[next_robot_pos] = grid[next_robot_pos], grid[robot_pos]
				robot_pos = next_robot_pos

			elif obstacle in ('[', ']'):
				todo = set()
				seen = set()
				seen.add(robot_pos)
				todo.add(next_robot_pos)
				if obstacle == '[':
					temp = vec.add(next_robot_pos, d['>'])
					todo.add(temp)
				else:
					temp = vec.add(next_robot_pos, d['<'])
					todo.add(temp)
				free_to_move = True
				while len(todo) > 0:
					next_obstacle_pos = todo.pop()
					if next_obstacle_pos not in seen:
						next_obstacle = grid[next_obstacle_pos]
						if next_obstacle in ('[', ']'):
							seen.add(next_obstacle_pos)
							todo.add(vec.add(order_dir, next_obstacle_pos))
							if next_obstacle == '[':
								temp = vec.add(next_obstacle_pos, d['>'])
								if temp not in seen:
									todo.add(temp)
							else:
								temp = vec.add(next_obstacle_pos, d['<'])
								if temp not in seen:
									todo.add(temp)
						if next_obstacle == '#':
							free_to_move = False
				if free_to_move:
					dx, dy = order_dir
					l = []
					if dx == 1:
						# right to left
						l = sorted(list(seen), reverse=True)
					if dx == -1:
						# left to right
						l = sorted(list(seen))
					if dy == -1:
						# up to down
						l = sorted(list(seen), key=lambda x: x[1])
					if dy == 1:
						# down to up
						l = sorted(list(seen), key=lambda x: x[1], reverse=True)
					for position in l:
						next_pos = vec.add(position, order_dir)
						grid[next_pos] = grid[position]
						grid[position] = '.'
						if position == robot_pos:
							robot_pos = next_pos

	#print_grid(grid, len(orders_str), robot_pos, (width, height), 'None')
	return [
		key
		for key, value in grid.items()
		if value == '['
	]

def get_distance(coors: list[tuple[int, int]]):
	return sum(
		(100 * y) + x
		for x, y in coors
	)

def test_second_star():
	assert 1448458 == get_distance(make_moves())
