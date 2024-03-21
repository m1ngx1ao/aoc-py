from api import file_reader

def get_value(line: str, replace_words: bool = False) -> int:
	if replace_words:
		numerals = 'one, two, three, four, five, six, seven, eight, nine'.split(', ')
		for i, d in enumerate(numerals):
			line = line.replace(d, d[0] + str(i + 1) + d[-1])
	digits = [digit for digit in line if ord(digit) <= ord('9')]
	return int(digits[0] + digits[-1])

def test_mini():
	assert 25 == get_value('2965')
	assert 44 == get_value('4')

def test_medi():
	assert 25 == get_value('ta2g9a65ag')
	assert 44 == get_value('t4ac')

def test_maxi():
	assert 25 == get_value('rtwone3fivej', replace_words=True)
	assert 44 == get_value('beliefourself', replace_words=True)

def test_first():
	assert 52974 == sum(
		get_value(line)
		for line in file_reader.get_lines('2023/01')
	)

def test_second():
	assert 53340 == sum(
		get_value(line, replace_words=True)
		for line in file_reader.get_lines('2023/01')
	)