


def solution(A):
	n = len(A)
	fib = [0, 1]
	flag = True
	while flag:
		nf = fib[-1] + fib[-2]
		if nf > n: break
		fib.append(nf)
	pos = {0:[], 1:[]}
	for i, x in enumerate(A): pos[x].append(i)
	# fibs = sorted(list(set(pos[1]) & set(fib)), reverse=True)
	fibs = sorted(list(set(fib)), reverse=True)
	ones = pos[1]

	path = 0



solution([0,0,0,1,1,0,1,0,0,0,0])