def add(v, w):
	return tuple(ve + we for ve, we in zip(v, w))

def sub(v, w):
	return tuple(ve - we for ve, we in zip(v, w))

def maxabs(v):
	return max(abs(ve) for ve in v)

def mul(v, num):
	result = 0, 0
	for _ in range(num):
		result = add(result, v)
	return result