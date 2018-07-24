def maxNum(maxNum=1000):
    a = 0
    b = 1
    while b < maxNum:
        print(b)
        a, b = b, a + b


def maxCount(maxCount=100):
    a = 0
    b = 1
    count = 0
    while count < maxCount:
        print(b)
        a, b = b, a + b
        count = count + 1

def maxCountList(maxCount=100):
	fiblist = [0,1]
	while len(fiblist) < maxCount:
		fiblist.append(fiblist[-1]+fiblist[-2])
	print fiblist
		
# maxNum(100)
# maxCount(10)
maxCountList(100)
