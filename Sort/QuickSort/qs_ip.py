
def partition(array, left, right, pivotIndex):
	pivotValue = array[pivotIndex]
	## move the pivot value to the end
	tempValue = array[right]
	array[pivotIndex] = tempValue
	array[right] = pivotValue

	storeIndex = left
	
	for x in range(left, right):
		if array[x] <= pivotValue:
			tempValue = array[x]
			array[x] = array[storeIndex]
			array[storeIndex] = tempValue
			storeIndex = storeIndex + 1
	
	tempValue = array[storeIndex]
	array[storeIndex] = array[right]
	array[right] = tempValue

	return storeIndex

def qs_ip(array, left, right):
	if (left < right):
		pivotIndex = left + (right-left)/2
		pivotIndex = partition(array, left, right, pivotIndex)

		qs_ip(array, left, pivotIndex-1)
		qs_ip(array, pivotIndex+1, right)

