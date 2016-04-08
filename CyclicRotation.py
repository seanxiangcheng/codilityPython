#~ https://codility.com/programmers/lessons/17/

#~ A zero-indexed array A consisting of N integers is given. Rotation of 
#~ the array means that each element is shifted right by one index, and 
#~ the last element of the array is also moved to the first place.
#~ 
#~ For example, the rotation of array A = [3, 8, 9, 7, 6] is 
#~ [6, 3, 8, 9, 7]. The goal is to rotate array A K times; 
#~ that is, each element of A will be shifted to the right by K indexes.

def solution(A, K):
    # write your code in Python 2.7
    A = list(A)
    if K<0:
        print "Error: Array must not be empty, and K must be nonnegative!"
        return -1
    if len(A)==0:
		return A
		
    K = K % len(A)
    
    return( A[-K:] + A[:-K] )
    
    
    
def main():
	l = range(5)
	print "l:    ", l
	print "l->1: ", solution(l, 1)
	print "l->2: ", solution(l, 2)


if __name__ == "__main__":
	main()
