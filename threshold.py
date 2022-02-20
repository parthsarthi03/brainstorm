
import numpy as np


def Average(lst):
    return sum(lst) / len(lst)


def calculate_threshold(datafile, binaryfile):

	data = np.genfromtxt(datafile, delimiter=",")


	target = np.genfromtxt(binaryfile, delimiter=",")


	total_data = np.concatenate([data])

	total_target = np.concatenate([target]).reshape(-1, 1)

	x = np.reshape(total_data[0], (3, 800))

	print(total_target.shape)

	average_clench_one = []
	average_clench_two = []
	average_clench_three = []

	average_relax_one = []
	average_relax_two = []
	average_relax_three = []


	for row in zip(total_data, total_target):

		x = np.reshape(row[0], (3, 800))

		if row[1] == 0:
			average_relax_one.append(np.mean(x[0]))
			average_relax_two.append(np.mean(x[1]))
			average_relax_three.append(np.mean(x[2]))

		else:
			average_clench_one.append(np.mean(x[0]))
			average_clench_two.append(np.mean(x[1]))
			average_clench_three.append(np.mean(x[2]))


	return {"AC1": Average(average_clench_one), 
			"AC2": Average(average_clench_two),  
			"AC3": Average(average_clench_three), 
			"AR1": Average(average_relax_one),
			"AR2": Average(average_relax_two),
			"AR3": Average(average_relax_three)
			}



print(calculate_threshold("data4.csv", "binary4.csv"))










