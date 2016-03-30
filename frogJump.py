

def solution(X, Y, D):
    # write your code in Python 2.7
    if X>Y or D<1:
        print "Error: Y has to be greater than X; D has to be positive!"
    return -((X-Y)//D)

def main():
	X, Y, D = 10, 85, 30
	print "X=%d, Y=%d, D=%d:  " % (X, Y, D)
	print "step = :", solution(X, Y, D)
	
	
if __name__ == "__main__":
	main()

