# https://codility.com/c/run/trainingCQE5HY-T9D
# Task description
# A binary gap within a positive integer N is any maximal sequence of 
# consecutive zeros that is surrounded by ones at both ends in the 
# binary representation of N.

# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(N):
    # write your code in Python 2.7
    # check positive integer
    if not isinstance(N, int) or N<1:
        print("Error: N has be positive integer!")
        return -1
    
    # convert int to bin
    binStr = bin(N)[2:]
    gap = 0
    gapMax = 0
    
    for s in binStr:
        if s == '1':
            gapMax = max(gapMax, gap)
            gap = 0
        else:
            gap += 1
    
    return(gapMax)

	
	
def main():
	Ns = [1, 17, 169, 7762, 820984]
	print "%-10s %-22s %-16s" % ("Number", "BinaryString", "BinaryGap")
	for n in Ns:
		print "%-10d %-22s %-16d" % (n, bin(n)[2:], solution(n))
		
	
if __name__ == "__main__":
	main()
