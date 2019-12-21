import sys

import matplotlib.pyplot as mp

x = [1,2,3,4,5,6,7]
y = [1,3,9,18,9,3,1]

mp.plot(x, y, 'bo-')
mp.savefig('file.png')