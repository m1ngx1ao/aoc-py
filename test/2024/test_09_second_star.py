from api import file_reader, parse
# 0..111....22222


def get_input() -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
	files : list[tuple[int, int]] = []
	num_str_line = file_reader.get_lines('2024/09')
	#num_str_line = ['12345']
	whitespaces = []
	sum_nums = 0
	for idx, num_str in enumerate(num_str_line[0]):
		num = int(num_str)
		if idx % 2 == 0:
			files.append((sum_nums, num))
		else:
			whitespaces.append((sum_nums, num))
		sum_nums += num
	return files, whitespaces
#00...111...2...333.44.5555.6666.777.888899
#0..111....22222
#02.111....2222.
#033119....222..
#0221112...22...
#02211122..2....
#022111222......

def get_next_pos_slot(idx_file: int, length_file: int,
		whitespaces_slots: list[tuple[int, int]]) -> int | None:
	for idx_whsp, length_whsp in whitespaces_slots:
		if idx_whsp <= idx_file:
			if length_file <= length_whsp:
				return idx_whsp
	return None

def get_idx_whitespace(whitespaces, next_idx) -> int|None:
	for idx, whsp in enumerate(whitespaces):
		if whsp[0] == next_idx:
			return idx
	return None

def fill_line() -> list[tuple[int, int]]:
	files, whitespaces_slots = get_input()
	files.reverse()
	for i, (idx_file, length_file) in enumerate(files):
		next_slot_index = get_next_pos_slot(idx_file, length_file, whitespaces_slots)
		if next_slot_index is not None:
			files[i] = (next_slot_index, length_file)
			idx = get_idx_whitespace(whitespaces_slots, next_slot_index)
			if idx is not None:
				whitespaces_slots[idx] = (next_slot_index + length_file, whitespaces_slots[idx][1] - length_file)
	files.reverse()
	return files

print(fill_line())

def get_value_of_line():
	files = fill_line()
	result = 0
	for id, (idx_file, length_file) in enumerate(files):
		for a in range(length_file):
			result += (a+idx_file) * id
	return result

def test_second_star():
	assert 6379677752410 == get_value_of_line()
