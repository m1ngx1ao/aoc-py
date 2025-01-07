from __future__ import annotations

class Grid(dict):

	@staticmethod
	def from_lines(lines: list[str]) -> Grid:
		result = Grid()
		for y, line in enumerate(lines):
			for x, fach in enumerate(line):
				result[(x, y)] = fach
		return result

	@staticmethod
	def from_lines_skip_last_line(lines: list[str]) -> Grid:
		result = Grid()
		for y, line in enumerate(lines[:-1]):
			for x, fach in enumerate(line):
				result[(x, y)] = fach
		return result

	def occurrences(self) -> dict[str, set[tuple[int, int]]]:
		return {
			c: {key for key, value in self.items() if value == c}
			for c in set(self.values())
		}

	def size(self) -> tuple[int, int]:
		hs_x, hs_y = 0, 0
		for x, y in self:
			hs_x = max(hs_x, x)
			hs_y = max(hs_y, y)
		return (hs_x + 1, hs_y + 1)
