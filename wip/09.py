from api import file_reader

# 0..111....22222

nums_str = file_reader.get_lines('2024/09')

def get_line():
	is_free_space = False
	index = 0
	line = []
	occurencies = {}
	amount = 0
	for num in nums_str[0]:
		num = int(num)
		if not is_free_space:
			occurencies[index] = num
			for _ in range(num):
				line.append(index)
				amount += 1
			index += 1
			is_free_space = True
		else:
			for _ in range (num):
				line.append(-1)
			is_free_space = False
	return line, amount, occurencies

def get_amount_minus_one(line, index) -> int:
	result = 0
	i = index
	while line[i] == -1:
		result += 1
		i += 1
	return result

def fill_line():
	line, amount, occurencies = get_line()
	x_back = len(line) - 1
	x_front = 0
	value_front = line[x_front]
	if x_front < amount:
		if value_front == -1:
			amount_minus_one = get_amount_minus_one(line, x_front)
			if line[x_back] != -1:
				amount_back = occurencies[line[x_back]]
				if amount_minus_one >= amount_back:
					for _ in range(amount_back):
						line[x_front], line[x_back] = line[x_back], line[x_front]
						x_front += 1
						x_back -= 1
				x_back -= 1
	return line

def get_value_of_line():
	line = fill_line()
	result = 0
	for x, value in enumerate(line):
		if value != -1:
			result += x * value
	return result

print(get_value_of_line())