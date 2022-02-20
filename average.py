
import numpy as np


def Average(lst):
    return sum(lst) / len(lst)




data1 = np.genfromtxt('data1.csv', delimiter=",")
data2 = np.genfromtxt('data2.csv', delimiter=",")
data3 = np.genfromtxt('data3.csv', delimiter=",")
data4 = np.genfromtxt('data4.csv', delimiter=",")
data5 = np.genfromtxt('data5.csv', delimiter=",")
data6 = np.genfromtxt('data6.csv', delimiter=",")
data7 = np.genfromtxt('data7.csv', delimiter=",")
data8 = np.genfromtxt('data8.csv', delimiter=",")
data9 = np.genfromtxt('data9.csv', delimiter=",")
data10 = np.genfromtxt('data10.csv', delimiter=",")



target1 = np.genfromtxt('binary1.csv', delimiter=",")
target2 = np.genfromtxt('binary2.csv', delimiter=",")
target3 = np.genfromtxt('binary3.csv', delimiter=",")
target4 = np.genfromtxt('binary4.csv', delimiter=",")
target5 = np.genfromtxt('binary5.csv', delimiter=",")
target6 = np.genfromtxt('binary6.csv', delimiter=",")
target7 = np.genfromtxt('binary7.csv', delimiter=",")
target8 = np.genfromtxt('binary8.csv', delimiter=",")
target9 = np.genfromtxt('binary9.csv', delimiter=",")
target10 = np.genfromtxt('binary10.csv', delimiter=",")



total_data = np.concatenate([data5])



total_target = np.concatenate([target5]).reshape(-1, 1)


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


print("AC1: ", Average(average_clench_one))
print("AC2: ", Average(average_clench_two))
print("AC3: ", Average(average_clench_three))

print("AR1: ", Average(average_relax_one))
print("AR2: ", Average(average_relax_two))
print("AR3: ", Average(average_relax_three))













