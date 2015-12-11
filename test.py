# s is the generated string
# r is the run suffix
# w is the remaining 'white' spaces
# callback returns the solution node found
def gen(s, r, w, callback):
	# found valid solution when
	if (len(s) == 25 and r == [] and w == 0):
		callback(s)
	
	if w > 0:
		gen(s + [0], r, w - 1, callback)
	if r != [] and (len(s) == 0 or s[-1] != 1):
		gen(s + [1] * r[0], r[1:], w, callback)

def print_solution(x):
	print x

r = map(int, '7 3 1 1 7'.split())
print r
s = []
gen(s, r, 25 - sum(r), print_solution)

r = map(int, '1 3 3 2 1 8 1'.split())
print r
s = []
gen(s, r, 25 - sum(r), print_solution)

