import time
from contextlib import contextmanager

@contextmanager
def timeblock(label):
    start = time.perf_counter()
    try:
        yield
    finally:
        end = time.perf_counter()
        print('{} : {}'.format(label, end - start))


prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
# Make a dictionary of all prices over 200
with timeblock('count'):
	n = 1000000
	while n > 0:
		n -= 1
		#Here I don't know how to elimitate the time of counting down
		p1 = {key: value for key, value in prices.items() if value > 200}
#print(p1)
with timeblock('count'):
	n = 1000000
	while n > 0:
		n -= 1
		p1 = dict((key, value) for key, value in prices.items() if value > 200)
#print(p1)
# Make a dictionary of tech stocks
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key: value for key, value in prices.items() if key in tech_names}
#print(p2)
p2 = {key: prices[key] for key in prices.keys() & tech_names }
#print(p2)
