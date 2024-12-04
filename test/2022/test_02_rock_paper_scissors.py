from api import file_reader

def get_total_score_first(lines: list[str]) -> int:
	return sum(
		get_score(*[
			# 1: rock, 2: paper, 3: scissors
			{'A' : 1, 'X' : 1, 'B' : 2, 'Y' : 2, 'C' : 3, 'Z' : 3}[e]
			for e in line.split(' ')
		])
		for line in lines
	)

# x lose, y draw, z win
#second star

def get_score(opponent: int, proponent: int) -> int:
	outcome_score = 6
	if (opponent - proponent) % 3 == 1:
		outcome_score = 0
	if opponent == proponent:
		outcome_score = 3
	return outcome_score + proponent

def test_first_example():
	lines = file_reader.get_lines('2022/02Example')
	assert 15 == get_total_score_first(lines)

def test_first():
	lines = file_reader.get_lines('2022/02')
	assert 11873 == get_total_score_first(lines)
