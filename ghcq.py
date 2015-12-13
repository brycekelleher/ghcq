import sys
from itertools import product
from itertools import chain

rows, cols = range(0, 3), range(0, 3)
#squares = [(x, y) for x, y in product(rows, cols)]
squares = list(product(rows, cols))

# create the initial values
values = dict(zip(squares, [[0, 1] for s in squares]))

def assign(values, xy, v):
	if v in values[xy]:
# parse the input grid

# eliminate a value

# if this is satisfied then the row or column is known
#(25 - sum(r)) - (len(r) - 1)

# fixme: replace this with a product
def display(values):
	for r in rows:
		print ''.join(['.' if len(values[(r, c)]) > 1 else str(values[(r, c)]) for c in cols])

def parse_runs(f, n):
	return [[int(x) for x in f.readline().split()] for l in range(n)]


with open('input') as f:
	rowdefs = parse_runs(f, 25)
	coldefs = parse_runs(f, 25)
