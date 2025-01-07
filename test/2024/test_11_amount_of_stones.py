import functools as ft
from api import file_reader, parse

@ft.cache
def recursive(blinks_left: int, num) -> int:
	if blinks_left == 0:
		return 1
	result = 0
	if num == 0:
		result+=recursive(blinks_left-1, 1)
	elif len(str(num)) % 2 == 0:
		s = str(num)
		le = int(len(s)/2)
		result+= recursive(blinks_left-1, int(s[0:le]))
		right = s[le:]
		for r in right:
			zero_counter = 0
			if r == 0:
				zero_counter+=1
		if zero_counter == len(right):
			result+= recursive(blinks_left-1, 0)
		else:
			result += recursive(blinks_left-1, int(right))
	else:
		result+=recursive(blinks_left-1, 2024 * num)
	return result

def get_result(blinks):
	return sum (
		recursive(blinks, num)
		for num in file_reader.get_lines('2024/11', parse.ints)[0]
	)

def test_first_star():
	assert 199982 == get_result(25)

def test_second_star():
	assert 237149922829154 == get_result(75)