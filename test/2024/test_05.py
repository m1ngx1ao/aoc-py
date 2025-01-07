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
O, E, W, N, S = [d[s] for s in 'OEWNS']
NE, SE, SW, NW = vec_add(N, E), vec_add(S, E), vec_add(S, W), vec_add(N, W)

lines = file_reader.get_lines('2024/05', parse.ints)
def get_input():
	result_sections = []
	result_updates = []
	num_pair_now = True
	for line in lines:
		if num_pair_now:
			if len(line) > 0:
				a, b = line
				result_sections.append((a, b))
			else:
				num_pair_now = False
		else:
			result_updates.append(line)
	return result_sections, result_updates

def get_result_of_update_line(sections, update_line):
	visited = set()
	in_update_line = set(update for update in update_line)
	for update in reversed(update_line):
		for front, back in sections:
			if update == front and back in in_update_line:
				if back not in visited:
					return 0
			visited.add(update)
	d = update_line[int((len(update_line)//2))]
	return d

def bubble_sorter(sections, update_line):
	result = [u for u in update_line]
	for idx in range(1, len(result)):
		for idx in range(1, len(result)):
			for front, back in sections:
				if {result[idx-1], result[idx]} <= {front, back}:
					if (result[idx-1], result[idx]) != (front, back):
						result[idx-1], result[idx] =  result[idx], result[idx-1]
	return result

def get_second_star():
	sections, update_lines = get_input()
	result = 0
	for update_line in update_lines:
		if 0 == get_result_of_update_line(sections, update_line):
			line = bubble_sorter(sections, update_line)
			result += get_result_of_update_line(sections, line)
	return result

def get_first_star():
	sections, update_lines = get_input()
	return sum(
		get_result_of_update_line(sections, update_line)
		for update_line in update_lines
	)

def test_first_star():
 assert 5747 == get_first_star()

def test_second_star():
 assert 5502 == get_second_star()