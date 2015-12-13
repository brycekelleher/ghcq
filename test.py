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

def gen_stack(r):
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

# r = map(int, '7 3 1 1 7'.split())
# print r
# s = []
# gen(s, r, 25 - sum(r), print_solution)
# 
# r = map(int, '1 3 3 2 1 8 1'.split())
# print r
# s = []
# gen(s, r, 25 - sum(r), print_solution)
r0 = map(int, '7 3 1 1 7'.split())
r1 = map(int, '1 3 3 2 1 8 1'.split())
r2 = map(int, '2 1 2 1 8 2 1'.split())
r3 = map(int, '7 1 2 1 1 1 3'.split())
r4 = map(int, '1 2 3 1 1 3 1 1 2'.split())
r5 = map(int, '3 1 1 1 1 5 1'.split())
r6 = map(int, '1 7 3 2 1'.split())
print "r4"
for i in  [x for x in gen_stack(r4)]:
	print i
print "r4 filtered"
for i in  [x for x in gen_stack(r4) if x[2] == 1 and x[6] == 1 and x[7] == 1 and x[10] == 1 and x[14] == 1 and x[15] == 1 and x[16] == 1 and x[18] == 1]:
	print i

print "r5"
for i in  [x for x in gen_stack(r5)]:
	print i
print "r4 filtered"
for i in  [x for x in gen_stack(r5) if x[2] == 1 and x[6] == 1 and x[11] == 1 and x[16] == 1 and x[20]]:
	print i

print "r6"
for i in  [x for x in gen_stack(r6)]:
	print i
print "r6 filtered"
for i in  [x for x in gen_stack(r6) if x[7] == 1 and x[9] == 1 and x[14] == 1 and x[22]]:
	print i


