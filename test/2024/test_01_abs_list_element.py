from api import file_reader, parse

def get_sorted_lists():
	number_pairs = file_reader.get_lines('2024/01', parse.ints)
	left, right = zip(*number_pairs)
	return sorted(left), sorted(right)

def test_first_star():
	assert 2264607 == sum(
		abs(left - right)
		for left, right in zip(*get_sorted_lists())
	)

def test_second_star():
	left, right = get_sorted_lists()
	assert 19457120 == sum(
		right.count(le) * le
		for le in left
	)