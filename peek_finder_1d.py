#Program to find the peak of a 1D array

from timeit import default_timer as timer #timeit.default_timer provides the best clock available on user's platform and version of Python automatically

def peakOf(lst, left, right):
	
	if(len(lst) == None):
		return 0

	mid = (left+right)//2

	if (not(mid == left) and lst[mid] < lst[mid-1]):
		return peakOf(lst, left, mid-1)
	elif (not (mid == right) and lst[mid] < lst[mid+1]):
		return peakOf(lst, mid+1, right)
	else:
		return lst[mid]


elements = [1, 2, 9, 4, 5, 6, 7, 8]

start = timer() #record start time

if not elements: #check for empty list
	peak = None
elif (len(elements) == 1): #peak of a single item is the item itself
	peak = elements[0]
else:
	peak = peakOf(elements, 0, len(elements)-1)

end = timer() #record end time

message = "The peak of the list is: {0}"
print(message.format(peak))

print("\n\nExecution time = {}".format(end-start))