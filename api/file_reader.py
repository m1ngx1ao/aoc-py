def get_lines(year_day: str) -> list[str]:
	with open(f'input/{year_day}.txt', 'r', encoding = 'utf-8') as f:
		result = f.read().splitlines()
		f.close()
	return result
