from itertools import count, cycle, repeat
import time

cnt=count(1,0.5)
print("Count:")
for i in cnt:
    if i>=20:
        break
    print(i)
    time.sleep(0.1)

val=[1,2,3,4,5,6]
cy=cycle(val)
'''print("Cycle:")
for i in cy:
    print(i)
    time.sleep(0.1)'''

rp=repeat(val)

for i in rp:
    print(i)