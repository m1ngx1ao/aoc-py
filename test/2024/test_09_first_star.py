from api import file_reader
# 0..111....22222

nums_str = file_reader.get_lines('2024/09')

def get_line():
	is_free_space = False
	index = 0
	result = []
	amount = 0
	for num in nums_str[0]:
		num = int(num)
		if not is_free_space:
			for _ in range(num):
				result.append(index)
				amount += 1
			index += 1
			is_free_space = True
		else:
			for _ in range (num):
				result.append(-1)
			is_free_space = False
	return result, amount

def fill_line():
	line, amount = get_line()
	for x_front, value_front in enumerate(line):
		if x_front < amount:
			if value_front == -1:
				found = False
				x_back = len(line) - 1
				while not found:
					if line[x_back] != -1:
						line[x_front], line[x_back] = line[x_back], line[x_front]
						found = True
					x_back -= 1
	return line

def get_value_of_line():
	line = fill_line()
	result = 0
	for x, value in enumerate(line):
		if value == -1:
			return result
		result += x * value

def test_first_star():
	assert 6360094256423 == get_value_of_line()