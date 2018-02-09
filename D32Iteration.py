import numpy as np
import time

eg = np.zeros(1000000)

start = time.perf_counter()
for i in range(len(eg)):
	temp = eg[i]
end = time.perf_counter()
print('Consumed time: ' + str(end - start))

it = iter(eg)
start = time.perf_counter()
try:
	while 1:
		temp = next(it)
except StopIteration:
	pass
end = time.perf_counter()
print('Consumed time: ' + str(end - start))
