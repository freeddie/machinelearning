def minOfList(pl):
	min = pl[0]
	index = 0
	for i in range(len(pl)):
		if pl[i] < min:
			min = pl[i]
			index = i
	return index

def sortedMP(sl):
	nl = []
	for i in range (len(sl)):
		nl.append(sl[minOfList(sl)])
		del sl[minOfList(sl)]
	return nl

def sortedInsert(sl):
	nl = []
	for i in sl:
		isInsert = False
		newNum = i
		for j in nl:
			if newNum <= j:
				nl.insert(nl.index(j),newNum)
				isInsert = True
				break
		if not isInsert:
			nl.append(newNum)
	return nl


l = [4,3,2,1,0,9,11,216526,11,11,0,0,0,0]

print(sortedInsert(l))
