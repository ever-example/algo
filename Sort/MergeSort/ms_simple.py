
def ms_simple_split(array):
	if (len(array) <= 1):
		return array

	#split the array
	midIndex = len(array)/2
	left = array[:midIndex]
	right = array[midIndex:]
	
	#further sub-divide the array
	left = ms_simple_split(left)
	right = ms_simple_split(right)
	
	return ms_simple_merge(left, right)

def ms_simple_merge(left, right):
	result = []

	while (len(left) > 0) or (len(right) > 0):
		if (len(left) > 0) and (len(right) > 0):
			if (left[0] <= right[0]):
				result = result + [left[0]]
				left = left[1:]
			else:
				result = result + [right[0]]
				right = right[1:]
		elif (len(left) > 0):
			result = result + [left[0]]
			left = left[1:]
		elif (len(right) > 0):
			result = result + [right[0]]
			right = right[1:]

	return result
