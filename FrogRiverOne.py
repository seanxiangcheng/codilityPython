#~ https://codility.com/programmers/lessons/2/
#~ A small frog wants to get to the other side of a river. The frog is 
#~ currently located at position 0, and wants to get to position X. 
#~ Leaves fall from a tree onto the surface of the river.
#~ 
#~ You are given a non-empty zero-indexed array A consisting of N integers 
#~ representing the falling leaves. A[K] represents the position where 
#~ one leaf falls at time K, measured in seconds.
#~ 
#~ The goal is to find the earliest time when the frog can jump to 
#~ the other side of the river. The frog can cross only when leaves 
#~ ppear at every position across the river from 1 to X. You may assume 
#~ that the speed of the current in the river is negligibly small, i.e. 
#~ the leaves do not change their positions once they fall in the river.
#~ 
#~ For example, you are given integer X = 5 and array A such that:
#~ 
  #~ A[0] = 1
  #~ A[1] = 3
  #~ A[2] = 1
  #~ A[3] = 4
  #~ A[4] = 2
  #~ A[5] = 3
  #~ A[6] = 5
  #~ A[7] = 4
#~ In second 6, a leaf falls into position 5. This is the earliest time 
#~ when leaves appear in every position across the river.
#~ 
#~ Write a function:
#~ 
#~ def solution(X, A)
#~ 
#~ that, given a non-empty zero-indexed array A consisting of N integers 
#~ and integer X, returns the earliest time when the frog can jump to 
#~ the other side of the river.
#~ 
#~ If the frog is never able to jump to the other side of the river, 
#~ the function should return −1.
#~ 
#~ For example, given X = 5 and array A such that:
#~ 
  #~ A[0] = 1
  #~ A[1] = 3
  #~ A[2] = 1
  #~ A[3] = 4
  #~ A[4] = 2
  #~ A[5] = 3
  #~ A[6] = 5
  #~ A[7] = 4
#~ the function should return 6, as explained above.
#~ 
#~ Assume that:
#~ 
#~ N and X are integers within the range [1..100,000];
#~ each element of array A is an integer within the range [1..X].
#~ Complexity:
#~ 
#~ expected worst-case time complexity is O(N);
#~ expected worst-case space complexity is O(X), beyond input storage 
#~ (not counting the storage required for input arguments).
#~ Elements of input arrays can be modified.

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
