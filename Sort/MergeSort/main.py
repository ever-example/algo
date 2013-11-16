import sys, os
__path = os.path.abspath('../')
sys.path.append(__path)
from Values import *

from ms_simple import *

print "unsorted values: "
print values

print "performing ms_simple_split: "
print ms_simple_split(values)
