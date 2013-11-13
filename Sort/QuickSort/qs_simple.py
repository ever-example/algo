import sys, os
__path = os.path.abspath('../')
sys.path.append(__path)
from Values import *

def qs_simple(array):
	length = len(array)
	if (length <= 1):
		return array
	greater = []
	less = []
	pivot = array[length/2]
	array.pop(length/2)
	for x in array:
		if (x <= pivot):
			less.append(x)
		else:
			greater.append(x)
	return qs_simple(less) + [pivot] + qs_simple(greater)
			
