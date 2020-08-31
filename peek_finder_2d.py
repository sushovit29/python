#Program to find the peak of a 1D array

from timeit import default_timer as timer #timeit.default_timer provides the best clock available on user's platform and version of Python automatically

def globalPeak(lst):
	pass


def peakOf():
	pass


elements = [[00, 00, 00, 10, 00],
			[00, 14, 13, 12, 00],
			[00, 15, 10, 11, 17],
			[21, 16, 17, 19, 20],
			[00, 00, 00, 00, 00]]

start = timer() #record start time

if not elements: #check for empty list
	peak = None
elif (len(elements) == 1): #peak of a single item is the item itself
	peak = elements[0]
else:
	peak = peakOf()

end = timer() #record end time

message = "The peak of the list is: {0}"
print(message.format(peak))

print("\n\nExecution time = {}".format(end-start))