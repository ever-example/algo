import sys, os
__path = os.path.abspath('../')
sys.path.append(__path)
from Values import *

from qs_simple import *

print "unsorted: " 
print values

print "running QuickSort(simple): " 
print qs_simple(values)
