import sys, os
__path = os.path.abspath('../')
sys.path.append(__path)
from Values import *

from qs_simple import *
from qs_ip import *

print
print "unsorted: " 
print values
print

print "running QuickSort(simple): " 
print qs_simple(values[:])
print

print "running Partition once at index: " + str(length/2) + \
		" (value of " + str(values[length/2]) + "): "
print partition(values[:],0, length-1, length/2)[1];
print

print "running QuickSort(in place): "
print qs_ip(values[:], 0, length-1)
print

