def maxCountList(maxCount=100):	
	fiblist = [3,0,2]
	while len(fiblist) < maxCount:
		fiblist.append(fiblist[-2]+fiblist[-3])
	print fiblist
maxCountList(10)