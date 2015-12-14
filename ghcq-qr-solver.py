from itertools import product

# s is the generated string
# r is the run suffix
# w is the remaining 'white' spaces
# callback returns the solution node found
def gen_runs(r):
	l = []
	stack = []
	stack.append( ([], r, 25 - sum(r)) )
	while( len(stack) ):
		s, r, w = stack.pop(0)
		if (len(s) == 25 and r == [] and w == 0):
			l.append(s)

		if w > 0:
			stack.append( (s + [0], r, w - 1) )
		if r != [] and (len(s) == 0 or s[-1] != 1):
			stack.append( (s + [1] * r[0], r[1:], w) )

	return l

def run_matches(r, k):
	return all([True if type(k[i]) == list or k[i] == r[i] else False for i in range(25)])

def gen_runs_filtered(r, k):
	r = gen_runs(r)
	return [x for x in r if run_matches(x, k)]

# fixme: replace this with a product
def display(values):
	for r in range(25):
		print ''.join([str(values[(r, c)]) if (type(values[(r, c)]) != list) else '.' for c in range(25)])

def read_grid(f):
	knowns = []
	data = f.read()
	data = [x for x in data if x == '.' or x == '1' or x == '0']
	for s, d in zip(squares, data):
		if d == '0' or d == '1':
			values[s] = int(d)
			knowns.append(s)
	return knowns

def read_runs(f, n):
	return [[int(x) for x in f.readline().split()] for l in range(n)]

def all_zeros(z):
	return all([x == 0 for x in z])
def all_ones(z):
	return all([x == 1 for x in z])
def get_row_state(i, values):
	return [values[x] for x in rows[i]]
def get_col_state(i, values):
	return [values[x] for x in cols[i]]

# takes a line and all possibilities for that line as input
# for each element in the line - if it's uknown, check if it can now be solved,
# update it and push the element back onto the queue
def check_line(l, runs, q):
	z = zip(*runs)
	for i, s in enumerate(l):
		if type(values[s]) == list and all_zeros(z[i]):
			values[s] = 0
			q.append(s)
		if type(values[s]) == list and all_ones(z[i]):
			values[s] = 1
			q.append(s)

	return q

#######################################
#rows, cols = range(0, 25), range(0, 25)
squares = list(product(range(25), range(25)))
rows = [[(r, c) for c in range(25)] for r in range(25)]
cols = [[(r, c) for r in range(25)] for c in range(25)]

# create the initial values
values = dict(zip(squares, [[0, 1] for s in squares]))

# read the input grid and runs
with open("initial_state") as f:
	knowns = read_grid(f)
with open('input') as f:
	rowdefs = read_runs(f, 25)
	coldefs = read_runs(f, 25)

# seed the initial squares to evaluate
q = []
for i in knowns:
	q.append(i)
while (len(q) > 0 ):
	print "len(q)", len(q)
	s = q.pop(0)
 	q = check_line(rows[s[0]], gen_runs_filtered(rowdefs[s[0]], get_row_state(s[0], values)), q)
 	q = check_line(cols[s[1]], gen_runs_filtered(coldefs[s[1]], get_col_state(s[1], values)), q)
display(values)

