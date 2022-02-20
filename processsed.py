

THRESHOLD_VALUE = 4000

array = [[1, 13, 6], [9, 4, 7], [19, 16, 2]]


arr = np.array(array)


avg_one = np.average(arr[:, 0])
avg_two = np.average(arr[:, 1])
avg_three = np.average(arr[:, 2])

if (avg_one + avg_two + avg_three) / 3 > THRESHOLD_VALUE:
	# send True 

else:
	#send False 


# count function

THRESHOLD_ONE_CLENCH = 100
THRESHOLD_TWO_CLENCH = 100
THRESHOLD_THREE_CLENCH = 100


THRESHOLD_ONE_UNCLENCH = 100
THRESHOLD_TWO_UNCLENCH = 100
THRESHOLD_THREE_UNCLENCH = 100




count = 0
for i in range(3):
	count = 0
	for j in range(201):
		if arr[i, j] > THRESHOLD_VALUE:
			count += 1











