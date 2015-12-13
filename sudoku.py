from itertools import product

def cross(a, b):
	return [x + y for x, y in product(a, b)]

digits = '123456789'
rows = 'abcdefghi'
cols = digits
squares = cross(rows, cols)
# replace this with a product
unitlist = [cross(rows, c) for c in cols] + [cross(r, cols) for r in rows] + [cross(rs, cs) for rs in [rows[0:3], rows[3:6], rows[6:9]] for cs in [cols[0:3], cols[3:6], cols[6:9]]]

# map a square to a list of units containing the square
units = dict(zip(squares, [[u for u in unitlist if s in u] for s in squares]))

# map a sqaure to all of it's peers
peers = dict(zip(squares, [set([i for u in units[s] for i in u]) - set('a1') for s in squares]))

# parse the grid
grid = '4 . . | . . . | 8 . 5'
[c for c in grid if c in digits or c in '0.']
