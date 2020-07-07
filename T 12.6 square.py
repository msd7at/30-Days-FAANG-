#   https://www.techiedelight.com/find-square-number-without-using-multiplication-division-operator/
def findSquare(num):

	odd = 1
	sq = 0

	# convert number to positive if it is negative
	num = abs(num)

	while num > 0:
		sq = sq + odd
		odd = odd + 2
		num = num - 1

	return sq


if __name__ == '__main__':

	print(findSquare(8))
	print(findSquare(20))
