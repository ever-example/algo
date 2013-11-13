import sys, os
__path = os.path.abspath('../')
sys.path.append(__path)
from Values import *

from qs_simple import *
from qs_ip import *

print "unsorted: " 
print values

print "running QuickSort(simple): " 
print qs_simple(values[:])

print "running QuickSort(in place): "
print qs_ip(values[:], 0, length-1)
