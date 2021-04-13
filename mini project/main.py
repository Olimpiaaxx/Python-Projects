from board import *
from checker import *



b = Board()
b.initialize()
b.put(1, 1, 'x')
b.put(1, 2, 'x')
b.put(1, 0, 'x')
b.show()
c = Checker(b, 3)
c.check(1,1)
print(c.check(1,1))
