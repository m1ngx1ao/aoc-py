from api import file_reader, parse

def get_result():
	num_pairs = file_reader.get_lines('2024/13', parse.ints)
	result = 0
	for third_idx in range(2, len(num_pairs), 4):
		a_x, a_y = num_pairs[third_idx-2]
		b_x, b_y = num_pairs[third_idx-1]
		result_x, result_y = num_pairs[third_idx]
		# first star wouldn't require these two lines
		result_x += 10000000000000
		result_y += 10000000000000
		b = (result_x * a_y - result_y * a_x) / (b_x * a_y - b_y * a_x)
		a = (result_x - b * b_x) / a_x
		if abs(a - round(a)) < 0.0000001 and abs(b - round(b)) < 0.0000001:
			result += 3 * a + b
	return int(result)

def test_second_star():
	assert 73267584326867 == get_result()