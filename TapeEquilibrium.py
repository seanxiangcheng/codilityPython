
def solution(A):
    # write your code in Python 2.7
    sumA = sum(A)   # sum of A
    minDiff = abs(2*A[0] - sumA) # P=1, minDiff
    sumP = A[0] # P=1, first part
    
    for n in A[1:-1]:
        sumP = sumP + n
        minDiff = min( minDiff, abs(2*sumP - sumA))
        
    return minDiff

def main():
	Xs = [10, 85, 30, 281]
	print Xs
	print "result = ", solution(Xs)
	
	
if __name__ == "__main__":
	main()

