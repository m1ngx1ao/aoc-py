from api import file_reader

def vec_add(v, w):
	return tuple(ve + we for ve, we in zip(v, w))

def vec_sub(v, w):
	return tuple(ve - we for ve, we in zip(v, w))

def vec_maxabs(v):
	return max(abs(ve) for ve in v)

def get_signum(e):
	if e > 0:
		return 1
	if e < 0:
		return -1
	return 0

def vec_signum(v):
	return tuple(get_signum(ve) for ve in v)

d = {
	"O": (0, 0),
	"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1),
	"E": (1, 0), "W": (-1, 0), "N": (0, -1), "S": (0, 1)
}

def solve(knots):
	lines = file_reader.get_lines('2022/09')
	visited = set()
	queue_pos = [d['O'] for _ in range(knots+1)]
	for line in lines:
		order, amount = line.split(" ")
		for _ in range(int(amount)):
			new_queue_pos = [vec_add(queue_pos[0], d[order])]
			for index in range(1, len(queue_pos)):
				sub = vec_sub(new_queue_pos[index - 1], queue_pos[index])
				if vec_maxabs(sub) == 2:
					new_queue_pos.append(vec_add(vec_signum(sub), queue_pos[index]))
				else:
					new_queue_pos.append(queue_pos[index])
			queue_pos = new_queue_pos
			visited.add(queue_pos[-1])
	return len(visited)

def test_first():
	assert 6269 == solve(1)

def test_second():
	assert 2557 == solve(9)
