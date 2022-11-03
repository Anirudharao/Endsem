from mymath import *
import mymath

print(pi)
print(area(2))

try:
    print(mymath._c)
except Exception as e:
    print(e)
finally:
    print("Done")