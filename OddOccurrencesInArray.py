#~ https://codility.com/programmers/lessons/17/

#~ A non-empty zero-indexed array A consisting of N integers is given. 
#~ The array contains an odd number of elements, and each element of the 
#~ array can be paired with another element that has the same value, 
#~ except for one element that is left unpaired.
#~ 
#~ For example, in array A such that:
#~ 
  #~ A[0] = 9  A[1] = 3  A[2] = 9
  #~ A[3] = 3  A[4] = 9  A[5] = 7
  #~ A[6] = 9
#~ the elements at indexes 0 and 2 have value 9,
#~ the elements at indexes 1 and 3 have value 3,
#~ the elements at indexes 4 and 6 have value 9,
#~ the element at index 5 has value 7 and is unpaired.


# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"


# solution1 works but not efficient
def solution1(A):
    # write your code in Python 2.7
    L = len(A)
    if L%2==0:
        print "Error: array length must be odd!"
    result = []
    for n in A:
        if n in res:
            result.remove(n)
        else:
            result.append(n)
    
    return result[0]

# solution works and is the most efficient
def solution(A):
    # write your code in Python 2.7
    if len(A)%2==0:
        print "Error: array length must be odd!"
    result = 0
    for n in A:
		result ^= n
    return result

def main():
	test = [1, 2, 1]
	print "test:  ", test
	print "result:", solution(test)
	
	
if __name__ == "__main__":
	main()
