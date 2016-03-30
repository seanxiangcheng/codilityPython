
def solution(A):
    # write your code in Python 2.7
    result = (2+len(A))*(len(A)+1)/2 - sum(A)
    return result

def main():
	A = [5, 2, 1, 4]
	print A
	print "result = ", solution(A)
	
	
if __name__ == "__main__":
	main()

