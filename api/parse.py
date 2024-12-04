import re

def ints(line: str) -> list[int]:
	return [
		int(e)
		for e in re.findall(r'-?\d+', line)
	]

def uints(line: str) -> list[int]:
	return [
		abs(e)
		for e in ints(line)
	]