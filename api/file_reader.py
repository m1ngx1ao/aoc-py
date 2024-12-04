from typing import Callable, TypeVar

T = TypeVar('T')

def get_lines(year_day: str, parser: Callable[[str], T] = lambda l: l) -> list[T]:
	with open(f'input/{year_day}.txt', 'r', encoding = 'utf-8') as f:
		lines = f.read().splitlines()
		f.close()
	return [parser(line) for line in lines]
