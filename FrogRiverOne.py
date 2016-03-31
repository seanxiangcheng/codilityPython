# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(X, A):
    # write your code in Python 2.7
    booleans = 0
    finalVal = 2**X - 1
    for i in xrange(len(A)):
        booleans |= 1<<(A[i]-1)
        if booleans == finalVal:
            return i
            
    return -1

def solution2(X, A):
	Xcount = [0] * X
	numLeft = X
	for i in xrange(len(A)):
		if Xcount[A[i]-1]==0:
			Xcount[A[i]-1] = 1
			numLeft -= 1
			if numLeft==0:
				return i
	return -1


    
    
    
def main():
	A = [1, 2, 3, 4, 2, 3, 5, 2, 1]
	X = max(A)
	print "A: ", A
	print "X: ", X
	print "Solution : ", solution(X, A)
	print "Solution2: ", solution2(X, A)


if __name__ == "__main__":
	main()
