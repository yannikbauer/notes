# This is a comment
# print('hello world!')

import numpy as np

print(np.add(1,2))

for i in range(10):
    if i % 2 == 0:
        print(i, 'even')
    elif i == 7:
        continue
    else:
        print(i, 'odd')