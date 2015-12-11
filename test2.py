# s is the generated string
# r is the run suffix
# w is the remaining 'white' spaces
# callback returns the solution node found
def gen_r(l, s, r, w, callback):
	# found valid solution when
	if (len(s) == 25 and r == [] and w == 0):
		callback(s, l)
		return
	
	if w > 0:
		gen_r(l, s + [0], r, w - 1, callback)
	if r != [] and (len(s) == 0 or s[-1] != 1):
		gen_r(l, s + [1] * r[0], r[1:], w, callback)

def print_solution(x, l):
	print x
	print l.append(x)

def gen(r):
	l = []
	gen_r(l, [], r, 25 - sum(r), print_solution)
	return l

r = map(int, list('73117'))
print r
print gen(r)
s = []

r = map(int, list('1332181'))
print r
print gen(r)

