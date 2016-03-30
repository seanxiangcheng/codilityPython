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
