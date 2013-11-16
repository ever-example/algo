
def partition(array, left, right, pivotIndex):
	pivotValue = array[pivotIndex]
	## swap the pivot value to the end
	tempValue = array[right]
	array[pivotIndex] = tempValue
	array[right] = pivotValue

	storeIndex = left
	
	## at the very end, the value inside storeIndex will get swapped with
	## the pivot value. This loop will perform partitioning with
	## respect to the position of storeIndex, and with respect to the value
	## of pivotValue
	for x in range(left, right):
		if array[x] <= pivotValue:
			tempValue = array[x]
			array[x] = array[storeIndex]
			array[storeIndex] = tempValue
			storeIndex = storeIndex + 1
	
	tempValue = array[storeIndex]
	array[storeIndex] = array[right]
	array[right] = tempValue

	return storeIndex, array

def qs_ip(array, left, right):
	if (left < right):
		# select a pivot index
		pivotIndex = left + (right-left)/2
		# paritition with respect to the pivot
		pivotIndex = partition(array, left, right, pivotIndex)[0]
		# recursively sort elemnts smaller than pivot
		qs_ip(array, left, pivotIndex-1)
		# recursively sort elements greater than pivot
		qs_ip(array, pivotIndex+1, right)
		return array

