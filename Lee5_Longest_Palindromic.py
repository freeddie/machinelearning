"""description:

"""
l = [1,6,9,2,3,7,5,4,0,-8,767]


def reverseList(l,low,high):
	if low < high:
		temp = l[low]
		l[low] = l[high]
		l[high] = temp
		reverseList(l,low+1,high-1)
	else:
		return

reverseList(l,0,len(l)-1)
print(l)

